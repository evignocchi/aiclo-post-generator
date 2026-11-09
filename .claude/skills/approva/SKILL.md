---
name: approva
description: Approva una bozza di post e la porta da bozze/ a post/, oppure aggiunge i numeri di un post pubblicato. Usala quando l'utente dice "approva", "questo va bene, approvalo", "pubblicato, ecco i numeri".
---

# Approvare un post e registrare i numeri

## Approvare
1. Trova la bozza in `bozze/<autore>/` (se l'utente non dice quale, chiedilo; se ce n'è una sola recente, proponi quella).
2. Se nella bozza ci sono note "da confermare" (frasi a nome dell'autore, dati da verificare), ricordale all'utente in una riga prima di approvare.
3. Lancia `python3 scripts/approva.py bozze/<autore>/<file>.md`. Lo script sposta post e immagini in `post/<autore>/`, aggiunge `stato: approvato` e salva le righe cambiate rispetto alla prima bozza.
4. Lancia `python3 scripts/controlla_post.py`.
5. Commit ("Approvato: <titolo>") e push.
6. Proponi di lanciare la skill `impara` se dall'ultima volta sono entrati almeno 3 post approvati.

## Numeri dopo la pubblicazione
1. Chiedi (se non li dà) impression, reazioni, commenti, condivisioni, salvataggi, data e link. Meglio a 7 giorni dalla pubblicazione.
2. `python3 scripts/metriche.py post/<autore>/<file>.md --pubblicato-il AAAA-MM-GG --link URL --impression N --reazioni N --commenti N --condivisioni N --salvataggi N`
3. Commit ("Numeri: <titolo>") e push, poi proponi la skill `impara`.
