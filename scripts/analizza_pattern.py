#!/usr/bin/env python3
"""Analizza i post approvati (post/<autore>/) e scrive:
- dati/pattern-post.json: le caratteristiche di ogni post e i suoi numeri;
- la parte automatica di guide/09-pattern-approvati.md (fra i marcatori AUTO).

Uso:
    python3 scripts/analizza_pattern.py

Lo usa la skill "impara" (.claude/skills/impara/), che poi trasforma i numeri in lezioni.
"""
import json
import re
import statistics
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comune import POST_DIR, ROOT, brief, file_post, leggi_front_matter, numero, sezioni  # noqa: E402

GUIDA = ROOT / "guide" / "09-pattern-approvati.md"
JSON = ROOT / "dati" / "pattern-post.json"
INIZIO, FINE = "<!-- AUTO:INIZIO -->", "<!-- AUTO:FINE -->"


def punteggio(fm):
    """Engagement pesato: commenti e condivisioni valgono più delle reazioni (obiettivo = conversazione).
    Se ci sono le impression, è per 1.000 impression; altrimenti è il totale pesato."""
    r, c, s, sv, imp = (numero(fm.get(k)) for k in ["reazioni", "commenti", "condivisioni", "salvataggi", "impression"])
    if all(v is None for v in (r, c, s, sv)):
        return None
    tot = (r or 0) + 3 * (c or 0) + 5 * (s or 0) + 4 * (sv or 0)
    return round(tot / imp * 1000, 1) if imp else round(tot, 1)


def hook_scelto(sez):
    testo = sez.get("## Hook alternativi", "")
    hooks = re.findall(r"(?m)^(\d)\.\s*(?:\*\*(.+?):?\*\*:?)?\s*(.+)$", testo)
    m = re.search(r"Scelto il \*\*n\. (\d)", testo)
    scelto = m.group(1) if m else None
    for n, meccanismo, frase in hooks:
        if n == scelto:
            return (meccanismo or "").strip(" :"), frase.strip()
    return "", ""


def caratteristiche(f):
    fm, corpo = leggi_front_matter(f.read_text(encoding="utf-8"))
    sez = sezioni(corpo)
    post = sez.get("## Post", "")
    righe = [r for r in post.splitlines() if r.strip()]
    visual = sez.get("## Visual", "")
    tipo_visual = (re.search(r"(?m)^Tipo:\s*(.+)$", visual) or [None, ""])[1]
    anomalia = (re.search(r"(?m)^Anomalia:\s*(.+)$", visual) or [None, ""])[1]
    prompt = (re.search(r"```\n(.*?)```", visual, re.S) or [None, ""])[1].strip()
    meccanismo, _ = hook_scelto(sez)
    b = brief(corpo)
    return {
        "file": f.relative_to(ROOT).as_posix(),
        "autore": fm.get("autore") or f.parent.name,
        "approvato_il": fm.get("approvato_il", ""),
        "pubblicato_il": fm.get("pubblicato_il", ""),
        "target": b.get("target", ""),
        "leva": b.get("leva", ""),
        "struttura": b.get("struttura", ""),
        "obiettivo": b.get("obiettivo", ""),
        "hook_meccanismo": meccanismo,
        "prima_riga": righe[0] if righe else "",
        "parole_prima_riga": len(righe[0].split()) if righe else 0,
        "parole": len(post.split()),
        "righe": len(righe),
        "numeri": len(re.findall(r"\d+(?:[.,]\d+)?%?", post)),
        "domande": post.count("?"),
        "nomina_aiclo": "aiclo" in post.lower(),
        "chiusura": righe[-1] if righe else "",
        "visual_tipo": tipo_visual.strip(),
        "visual_anomalia": anomalia.strip(),
        "visual_prompt": prompt,
        "visual_foto_vera": "foto vera" in tipo_visual.lower() or "Template L" in tipo_visual,
        "modifiche_dalla_bozza": sez.get("## Cosa è cambiato dalla bozza", ""),
        "metriche": {k: fm.get(k, "") for k in ["impression", "reazioni", "commenti", "condivisioni", "salvataggi"]},
        "punteggio": punteggio(fm),
    }


def media(xs):
    xs = [x for x in xs if x is not None]
    return round(statistics.mean(xs), 1) if xs else None


def tabella_per(posts, chiave, etichetta):
    gruppi = defaultdict(list)
    for p in posts:
        gruppi[p[chiave] or "—"].append(p)
    righe = [f"| {etichetta} | Post | Con numeri | Punteggio medio |", "|---|---:|---:|---:|"]
    for k, g in sorted(gruppi.items(), key=lambda kv: -(media([p['punteggio'] for p in kv[1]]) or -1)):
        con = [p for p in g if p["punteggio"] is not None]
        righe.append(f"| {k} | {len(g)} | {len(con)} | {media([p['punteggio'] for p in con]) or '—'} |")
    return "\n".join(righe)


def sezione_auto(posts):
    con = sorted([p for p in posts if p["punteggio"] is not None], key=lambda p: -p["punteggio"])
    out = [INIZIO, "", "_Parte generata da `scripts/analizza_pattern.py`: non modificarla a mano._", ""]
    out.append(f"**Post approvati:** {len(posts)} · **con i numeri di pubblicazione:** {len(con)}")
    if len(con) < 5:
        out.append("")
        out.append(f"⚠️ Servono almeno 5 post con i numeri per parlare di pattern (ora sono {len(con)}). "
                   "Fino ad allora le lezioni si basano soprattutto su cosa è stato modificato fra bozza e versione approvata.")
    out += ["", "### Medie dei post approvati",
            f"- Parole: {media([p['parole'] for p in posts])} · righe: {media([p['righe'] for p in posts])} · "
            f"parole della prima riga: {media([p['parole_prima_riga'] for p in posts])} · numeri nel testo: {media([p['numeri'] for p in posts])}",
            f"- Post che nominano Aiclo: {sum(p['nomina_aiclo'] for p in posts)} su {len(posts)}", ""]
    for chiave, etichetta in [("struttura", "Struttura"), ("hook_meccanismo", "Meccanismo dell'hook"),
                              ("target", "Target"), ("visual_tipo", "Tipo di visual"), ("autore", "Autore")]:
        out += [f"### Per {etichetta.lower()}", tabella_per(posts, chiave, etichetta), ""]
    out += ["### Classifica (solo post con i numeri)"]
    if con:
        out += ["| # | Post | Punteggio | Prima riga | Visual |", "|---:|---|---:|---|---|"]
        for i, p in enumerate(con, 1):
            out.append(f"| {i} | `{p['file']}` | {p['punteggio']} | {p['prima_riga']} | {p['visual_tipo']} |")
    else:
        out.append("Ancora nessun post con i numeri. Dopo la pubblicazione: `python3 scripts/metriche.py post/... --reazioni N --commenti N ...`")
    out += ["", "### Tutte le prime righe approvate"]
    out += [f"- {p['prima_riga']} _({p['hook_meccanismo'] or 'meccanismo n.d.'} · {p['autore']})_" for p in posts]
    out += ["", "### Prompt delle visual approvate"]
    for p in posts:
        if p["visual_prompt"]:
            out += [f"**{p['file']}** · {p['visual_tipo']} · punteggio {p['punteggio'] or '—'}",
                    f"Anomalia: {p['visual_anomalia'] or 'n.d.'}", "```", p["visual_prompt"], "```", ""]
    out += ["", FINE]
    return "\n".join(out)


def main():
    posts = [caratteristiche(f) for f in file_post(POST_DIR)
             if leggi_front_matter(f.read_text(encoding="utf-8"))[0].get("stato") == "approvato"]
    JSON.write_text(json.dumps(posts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    testo = GUIDA.read_text(encoding="utf-8")
    nuovo = re.sub(re.escape(INIZIO) + r".*?" + re.escape(FINE), lambda _: sezione_auto(posts), testo, flags=re.S)
    GUIDA.write_text(nuovo, encoding="utf-8")
    print(f"Analizzati {len(posts)} post approvati → {JSON.relative_to(ROOT)} e {GUIDA.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
