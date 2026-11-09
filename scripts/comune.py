"""Funzioni comuni agli script dei post: front matter, sezioni, parsing del brief."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POST_DIR = ROOT / "post"
BOZZE_DIR = ROOT / "bozze"
FILE_NON_POST = {"profilo.md", "post-pubblicati.md", "README.md"}

CAMPI_FRONT_MATTER = [
    "stato", "autore", "approvato_il", "pubblicato_il", "link",
    "impression", "reazioni", "commenti", "condivisioni", "salvataggi",
]
SEZIONI_OBBLIGATORIE = ["## Hook alternativi", "## Post", "## Visual", "## Checklist"]


def leggi_front_matter(testo):
    """Ritorna (dict, corpo). Front matter semplice: righe 'chiave: valore' fra due '---'."""
    if not testo.startswith("---\n"):
        return {}, testo
    fine = testo.find("\n---\n", 4)
    if fine == -1:
        return {}, testo
    dati = {}
    for riga in testo[4:fine].splitlines():
        if ":" in riga:
            k, v = riga.split(":", 1)
            dati[k.strip()] = v.strip()
    return dati, testo[fine + 5:].lstrip("\n")


def scrivi_front_matter(dati, corpo):
    righe = ["---"]
    for k in CAMPI_FRONT_MATTER:
        righe.append(f"{k}: {dati.get(k, '')}".rstrip())
    for k, v in dati.items():
        if k not in CAMPI_FRONT_MATTER:
            righe.append(f"{k}: {v}".rstrip())
    righe.append("---")
    return "\n".join(righe) + "\n\n" + corpo.lstrip("\n")


def sezioni(corpo):
    """Dizionario {titolo sezione '## X': testo}."""
    out = {}
    parti = re.split(r"(?m)^(## .+)$", corpo)
    for i in range(1, len(parti), 2):
        out[parti[i].strip()] = parti[i + 1].strip("\n")
    return out


def brief(corpo):
    """Estrae autore e campi del brief dalla riga '**Autore** — … · **Brief** — Target: … · Leva: …'."""
    out = {}
    m = re.search(r"\*\*Autore\*\*\s*—\s*(.+?)\s*·\s*\*\*Brief\*\*\s*—\s*(.+)", corpo)
    if not m:
        return out
    out["autore"] = m.group(1).strip()
    for pezzo in m.group(2).split("·"):
        if ":" in pezzo:
            k, v = pezzo.split(":", 1)
            out[k.strip().lower()] = v.strip()
    return out


def file_post(cartella):
    """Tutti i file di post (esclusi profili, README e template) sotto una cartella."""
    for f in sorted(cartella.glob("*/*.md")):
        if f.name in FILE_NON_POST or f.parent.name.startswith("_"):
            continue
        yield f


def numero(v):
    try:
        return float(str(v).replace(".", "").replace(",", "."))
    except (TypeError, ValueError):
        return None
