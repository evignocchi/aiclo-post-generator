# Istruzioni per generare i post LinkedIn di Aiclo

Questa repository è una **macchina per scrivere post LinkedIn** che escono dai **profili personali** del team Aiclo (conversation intelligence per i team di vendita delle PMI italiane).

**Obiettivo unico: engagement** (reazioni, commenti, condivisioni). Non si vendono demo. Il post deve valere anche per chi non comprerà mai Aiclo.

## Prima di scrivere, leggi
1. `post/<autore>/profilo.md` (e `post-pubblicati.md`, se c'è): chi firma il post, la sua voce, i suoi temi **(obbligatorio)**
2. `guide/02-anatomia-post-vincente.md`: le 10 leggi e le 6 strutture **(obbligatorio)**
3. `guide/04-mappa-empatia.md`: a chi parli e quale nervo tocchi **(obbligatorio)**
4. `guide/05-tono-di-voce.md`: come parli e fin dove si può provocare **(obbligatorio)**
5. `guide/06-hook-e-chiusure.md`: i meccanismi per l'apertura e la chiusura
6. `dati/`: insight aggregati (solo le righe con `Approvato: sì`), episodi e clienti da usare come spunto
7. `guide/03-icp-aiclo.md`: il prodotto e i claim pubblici
8. `guide/07-prompt-grafiche.md`: brand e prompt, solo se il post richiede un visual
9. `guide/01-analisi-post-benchmark.md`: per approfondire perché le regole sono queste

## Procedura
1. **Autore.** Se l'utente non lo indica, chiedilo. Leggi il suo `profilo.md` e gli ultimi 5 post nella sua cartella, per non ripetere temi, hook o strutture.
2. **Brief** (se l'utente non lo dà, sceglilo tu e scrivilo in testa all'output):
   - Target: Manager | Venditore. **Alternali**: guarda gli ultimi post dell'autore e scegli il target meno usato di recente.
   - Leva emotiva (dalla tabella del file `04`)
   - Struttura: S1-S6 o Meme
   - Obiettivo: commenti | condivisioni | salvataggi
   - Materiale reale: insight, episodio o cliente dalla cartella `dati/`
3. **Scrivi 3 hook alternativi** con meccanismi diversi e scegli il migliore.
4. **Scrivi il post** con la struttura scelta e la voce dell'autore.
5. **Passa la checklist** di `guide/08-checklist-qualita.md` e correggi.
6. **Decidi il visual** con la tabella del file `07`. Se serve, scrivi il prompt completo partendo dal template e usando i colori del brand.
7. **Salva** in `post/<autore>/AAAA-MM-GG-slug.md`.

Quantità: **a richiesta**. Se vengono chiesti più post insieme, variare autore, target e struttura.

## Formato dell'output (sempre questo)
```markdown
# [Titolo interno del post]

**Autore** — … · **Brief** — Target: … · Leva: … · Struttura: … · Obiettivo: …
**Fonti dati** — [riga di dati/… usata, "storia costruita", "numero costruito", oppure "nessuna"]

## Hook alternativi
1. …
2. …
3. …

## Post
[testo pronto da incollare]

## Visual
Tipo: [nessuno | metafora | card trascrizione | tipografica | carosello | meme | screenshot | foto reale]
Prompt:
[prompt completo, pronto da incollare nel generatore]
(oppure: "Nessun visual: testo semplice.")

## Primo commento (facoltativo)
…

## Checklist
[punteggio x/15 e i punti mancati]
```

## Regole non negoziabili
- **Le storie si possono costruire.** Prima e dopo, scene di trattativa, clienti tipo, frasi di manager e venditori: si possono inventare, purché siano verosimili, anonime (mai un'azienda o una persona reale con il nome) e coerenti con il prodotto e con i clienti tipici del file `03`. I numeri dentro una singola storia (il tasso di chiusura di un venditore, il minuto di una trattativa) si possono costruire. Nell'output, alla voce **Fonti dati**, scrivi `storia costruita`, così l'autore lo sa prima di pubblicare.
- **I numeri si possono costruire**, se sono presentati come esperienza dell'autore ("su 10 'ci penso' che ricevo, ne chiudo 2"), come esempio o dentro una storia. Nell'output, alla voce **Fonti dati**, scrivi `numero costruito`, così l'autore lo verifica con la sua esperienza prima di pubblicare.
- **Unico limite:** un numero presentato come risultato dell'analisi di Aiclo ("nelle 10.000 trattative che abbiamo analizzato, il X%…") viene solo dai claim del file `03` o dalle righe approvate in `dati/`. Mai citazioni inventate attribuite a persone reali con il nome.
- **Il dato "63% delle vendite sul territorio" non si usa**: non ha una fonte.
- **Aiclo quasi mai nominato**: l'obiettivo è l'engagement. Al massimo 1 post su 8 lo nomina, una sola volta e mai nella prima riga.
- **Si provoca un pensiero, mai una persona.** Niente attacchi, niente presunzione, niente tono da "io ho capito e voi no" (vedi il file `05`).
- Mai nominare i concorrenti, mai usare la paura del licenziamento come leva, mai presentare Aiclo come uno strumento di controllo.
- I clienti si citano solo come previsto in `dati/clienti-e-risultati.md`.
- In italiano. Niente parole vietate (file `05`).

## Aggiungere un autore
Copia `post/_template-autore/` in `post/nome-cognome/`, compila `profilo.md` e aggiungi l'autore alla tabella in `post/README.md`.
