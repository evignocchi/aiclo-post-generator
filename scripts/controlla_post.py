#!/usr/bin/env python3
"""Controlla che in post/<autore>/ ci siano solo post approvati e completi.
Lo lancia la GitHub Action ad ogni push; si può lanciare anche a mano:

    python3 scripts/controlla_post.py
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comune import POST_DIR, ROOT, SEZIONI_OBBLIGATORIE, file_post, leggi_front_matter  # noqa: E402


def main():
    errori = []
    for f in file_post(POST_DIR):
        rel = f.relative_to(ROOT)
        fm, corpo = leggi_front_matter(f.read_text(encoding="utf-8"))
        if fm.get("stato") != "approvato":
            errori.append(f"{rel}: non è approvato. Le bozze vanno in bozze/{f.parent.name}/ e si approvano con scripts/approva.py")
            continue
        for s in SEZIONI_OBBLIGATORIE:
            if s not in corpo:
                errori.append(f"{rel}: manca la sezione {s}")
        for img in set(re.findall(r"img/[\w\-.]+", corpo)):
            if not (f.parent / img).exists():
                errori.append(f"{rel}: immagine mancante {img}")
    for img in POST_DIR.glob("*/img/*"):
        if not any(img.name in p.read_text(encoding="utf-8") for p in img.parent.parent.glob("*.md")):
            errori.append(f"{img.relative_to(ROOT)}: immagine non usata da nessun post approvato")
    if errori:
        print("\n".join(errori))
        sys.exit(1)
    print("OK: in post/ ci sono solo post approvati.")


if __name__ == "__main__":
    main()
