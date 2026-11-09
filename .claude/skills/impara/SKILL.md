---
name: impara
description: Impara dai post approvati e migliora le regole di scrittura e i prompt delle immagini. Usala quando l'utente dice "impara", "aggiorna i pattern", "cosa funziona?", dopo aver approvato nuovi post o dopo aver aggiunto i numeri di pubblicazione.
---

# Impara dai post approvati

Questo è il ciclo di apprendimento della macchina: non è un fine-tuning del modello, è un aggiornamento delle regole che il modello legge prima di scrivere. Così ogni miglioramento è visibile, si può discutere e si può annullare con git.

## Passi
1. Lancia `python3 scripts/controlla_post.py` e poi `python3 scripts/analizza_pattern.py`.
2. Leggi `guide/09-pattern-approvati.md` (parte automatica e lezioni attuali) e `dati/pattern-post.json`.
3. Leggi per intero i post approvati più recenti e, se ci sono i numeri, i 3 migliori e i 3 peggiori.
4. Per ogni post leggi la sezione **"Cosa è cambiato dalla bozza"**: ogni riga tolta o riscritta da un umano è un'indicazione su cosa non va nelle bozze (parole, tono, lunghezza, tipo di hook, promesse troppo forti).
5. Cerca i pattern su questi assi:
   - **Scrittura:** meccanismo dell'hook, lunghezza della prima riga, struttura, target, leva, lunghezza totale, quanti numeri, tipo di chiusura, autore.
   - **Visual:** tipo, anomalia, foto vera o generata, colori, cosa è stato rifatto in revisione, prompt dei post migliori.
6. Aggiorna la sezione **Lezioni** di `guide/09-pattern-approvati.md`:
   - una riga per lezione, con la **prova** (quali post) e la **confidenza** (bassa 1-2 post, media 3-5, alta 6+ con i numeri);
   - alza o abbassa la confidenza delle lezioni esistenti; togli quelle smentite e spostale in "Da verificare" se i dati non bastano;
   - in "Prompt immagini che hanno funzionato" tieni i migliori (massimo 5), descritti in modo riutilizzabile.
7. Solo con confidenza **media o alta**, porta la lezione nei file di riferimento:
   - hook che funzionano → `guide/06-hook-e-chiusure.md` (aggiungili come esempi approvati, con il file di provenienza);
   - regole di scrittura → `guide/02-anatomia-post-vincente.md` o `guide/05-tono-di-voce.md`;
   - visual e prompt → `guide/07-prompt-grafiche.md` (template e regole);
   - voce di un autore → il suo `post/<autore>/profilo.md`.
8. Fai un riepilogo all'utente: cosa hai imparato, cosa hai cambiato e dove, cosa serve ancora (per esempio "mancano i numeri di 4 post").
9. Commit con messaggio "Impara: ..." e push.

## Limiti
- **Mai** cambiare le regole non negoziabili di `CLAUDE.md` (dati attribuiti ad Aiclo veri, niente nomi di clienti, Aiclo quasi mai nominato, si provoca un pensiero e non una persona, niente concorrenti, niente paura del licenziamento).
- Con meno di 5 post con i numeri non si parla di "cosa funziona", ma di "cosa preferiamo in revisione".
- Una lezione nuova non deve contraddire senza prove una lezione con confidenza più alta.
