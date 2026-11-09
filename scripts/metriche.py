#!/usr/bin/env python3
"""Aggiunge o aggiorna i numeri reali di un post approvato, dopo la pubblicazione.

Uso:
    python3 scripts/metriche.py post/<autore>/AAAA-MM-GG-slug.md \
        --pubblicato-il 2026-11-12 --link https://... \
        --impression 8200 --reazioni 140 --commenti 37 --condivisioni 6 --salvataggi 12

Si può rilanciare quando i numeri crescono (per esempio dopo 48 ore e dopo 7 giorni).
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comune import POST_DIR, ROOT, leggi_front_matter, scrivi_front_matter  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("post")
    for campo in ["pubblicato-il", "link", "impression", "reazioni", "commenti", "condivisioni", "salvataggi"]:
        ap.add_argument(f"--{campo}")
    a = ap.parse_args()

    f = (ROOT / a.post).resolve()
    if POST_DIR not in f.parents or not f.exists():
        sys.exit("Indica un post approvato dentro post/<autore>/.")
    fm, corpo = leggi_front_matter(f.read_text(encoding="utf-8"))
    if fm.get("stato") != "approvato":
        sys.exit("Il post non è approvato: prima usa scripts/approva.py.")
    for k, v in vars(a).items():
        if k != "post" and v is not None:
            fm[k] = v
    f.write_text(scrivi_front_matter(fm, corpo), encoding="utf-8")
    print(f"Aggiornato: {f.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
