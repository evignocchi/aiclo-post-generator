#!/usr/bin/env python3
"""Approva una bozza: la sposta da bozze/<autore>/ a post/<autore>/ con le immagini,
aggiunge il front matter 'stato: approvato' e salva cosa è cambiato rispetto alla prima bozza.

Uso:
    python3 scripts/approva.py bozze/<autore>/AAAA-MM-GG-slug.md [--data AAAA-MM-GG]

Poi: git add -A && git commit -m "Approvato: ..." && git push
"""
import argparse
import datetime
import difflib
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comune import (BOZZE_DIR, POST_DIR, ROOT, SEZIONI_OBBLIGATORIE, brief,  # noqa: E402
                    leggi_front_matter, scrivi_front_matter, sezioni)

TITOLO_DIFF = "## Cosa è cambiato dalla bozza"


def git(*args):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def prima_versione(percorso):
    """Testo della prima versione committata del file (seguendo gli spostamenti), o None."""
    rel = percorso.relative_to(ROOT).as_posix()
    log = git("log", "--follow", "--format=@%H", "--name-only", "--", rel).split("@")
    voci = [v.split() for v in log if v.strip()]
    if not voci:
        return None
    commit, vecchio_nome = voci[-1][0], voci[-1][-1]
    return git("show", f"{commit}:{vecchio_nome}") or None


def riassunto_modifiche(prima, dopo):
    """Righe tolte e aggiunte nel testo del post, fra la prima bozza e la versione approvata."""
    p = sezioni(leggi_front_matter(prima)[1]).get("## Post", "").splitlines()
    d = sezioni(leggi_front_matter(dopo)[1]).get("## Post", "").splitlines()
    tolte = [r[2:] for r in difflib.ndiff(p, d) if r.startswith("- ") and r[2:].strip()]
    aggiunte = [r[2:] for r in difflib.ndiff(p, d) if r.startswith("+ ") and r[2:].strip()]
    if not tolte and not aggiunte:
        return "Nessuna modifica al testo del post rispetto alla prima bozza."
    out = ["Righe del post cambiate fra la prima bozza e la versione approvata (servono per imparare: vedi `guide/09`)."]
    if tolte:
        out += ["", "Tolte:"] + [f"- ~~{r}~~" for r in tolte]
    if aggiunte:
        out += ["", "Aggiunte:"] + [f"- {r}" for r in aggiunte]
    return "\n".join(out)


def sposta(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if git("ls-files", "--error-unmatch", src.relative_to(ROOT).as_posix()):
        subprocess.run(["git", "mv", "-f", str(src), str(dst)], cwd=ROOT, check=True)
    else:
        shutil.move(str(src), str(dst))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bozza")
    ap.add_argument("--data", default=datetime.date.today().isoformat(), help="data di approvazione")
    a = ap.parse_args()

    src = (ROOT / a.bozza).resolve() if not Path(a.bozza).is_absolute() else Path(a.bozza)
    if not src.exists():
        sys.exit(f"Non trovo {a.bozza}")
    if BOZZE_DIR not in src.parents:
        sys.exit("Si approvano solo i file dentro bozze/<autore>/.")
    autore = src.parent.name

    testo = src.read_text(encoding="utf-8")
    fm, corpo = leggi_front_matter(testo)
    mancanti = [s for s in SEZIONI_OBBLIGATORIE if s not in corpo]
    if mancanti:
        sys.exit(f"Bozza incompleta, mancano le sezioni: {', '.join(mancanti)}")
    if not brief(corpo):
        sys.exit("Manca la riga **Autore** — … · **Brief** — …")
    if "[DATO DA INSERIRE]" in sezioni(corpo).get("## Post", ""):
        sys.exit("Il post contiene ancora [DATO DA INSERIRE].")

    # cosa è cambiato rispetto alla prima bozza
    prima = prima_versione(src)
    diff = riassunto_modifiche(prima, testo) if prima else "Prima versione non trovata in git (bozza mai committata)."
    corpo = re.sub(rf"\n{re.escape(TITOLO_DIFF)}\n.*?(?=\n## |\Z)", "", corpo, flags=re.S).rstrip()
    corpo += f"\n\n{TITOLO_DIFF}\n{diff}\n"

    fm.update({"stato": "approvato", "autore": autore, "approvato_il": a.data})
    dst = POST_DIR / autore / src.name

    # immagini referenziate come img/...
    nomi = set(re.findall(r"img/[\w\-.]+", corpo))
    nomi |= {f"img/{f.name}" for f in (src.parent / "img").glob(f"{src.stem}*")}
    for nome in sorted(nomi):
        img_src, img_dst = src.parent / nome, dst.parent / nome
        if img_src.exists():
            sposta(img_src, img_dst)

    sposta(src, dst)
    dst.write_text(scrivi_front_matter(fm, corpo), encoding="utf-8")
    print(f"Approvato: {dst.relative_to(ROOT)}")
    print("Dopo la pubblicazione aggiungi i numeri con: python3 scripts/metriche.py", dst.relative_to(ROOT), "--reazioni N --commenti N ...")


if __name__ == "__main__":
    main()
