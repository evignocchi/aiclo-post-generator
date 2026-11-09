# Bozze

Qui finiscono **tutti i post generati**, una cartella per autore: `bozze/<autore>/AAAA-MM-GG-slug.md` (immagini in `bozze/<autore>/img/`).

In `post/<autore>/` entrano **solo i post approvati**: un controllo automatico (`scripts/controlla_post.py`, lanciato dalla GitHub Action) blocca tutto il resto.

## Il ciclo
1. **Genera** → la bozza viene salvata qui e committata (così non si perde e si vede cosa cambia).
2. **Rivedi** → si modifica la bozza qui (hook, testo, visual).
3. **Approva** → `python3 scripts/approva.py bozze/<autore>/<file>.md` (o chiedi a Claude "approva"). Il post passa in `post/<autore>/` con `stato: approvato` e con le righe cambiate rispetto alla prima bozza.
4. **Pubblica e misura** → dopo 7 giorni: `python3 scripts/metriche.py post/<autore>/<file>.md --reazioni N --commenti N ...`
5. **Impara** → chiedi a Claude "impara": aggiorna `guide/09-pattern-approvati.md` e, quando le prove bastano, le guide di scrittura e i prompt delle immagini.

Le bozze scartate si cancellano (resta comunque la storia in git).
