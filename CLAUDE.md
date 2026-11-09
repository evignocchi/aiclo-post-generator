# Istruzioni per generare i post LinkedIn di Aiclo

Questa repository è una **macchina per scrivere post LinkedIn** per Aiclo (conversation intelligence per i team di vendita delle PMI italiane). Quando ti viene chiesto un post, segui questa procedura.

## Prima di scrivere, leggi
1. `guide/02-anatomia-post-vincente.md`: le 10 leggi e le 6 strutture **(obbligatorio)**
2. `guide/04-mappa-empatia.md`: a chi parli e quale nervo tocchi **(obbligatorio)**
3. `guide/05-tono-di-voce.md`: come parli **(obbligatorio)**
4. `guide/06-hook-e-chiusure.md`: i meccanismi per l'apertura e la chiusura
5. `guide/03-icp-aiclo.md`: il prodotto e i claim utilizzabili
6. `guide/07-prompt-grafiche.md`: solo se il post richiede un visual
7. `guide/01-analisi-post-benchmark.md`: per approfondire perché le regole sono queste

## Procedura
1. **Definisci il brief** (se l'utente non lo dà, sceglilo tu e scrivilo in testa all'output):
   - Target: Manager | Venditore | Entrambi
   - Leva emotiva (dalla tabella "Leve emotive" del file `04`)
   - Struttura: S1-S6 o Meme
   - Obiettivo: commenti | condivisioni | salvataggi | autorevolezza
   - Materiale reale disponibile (dato, episodio, trascrizione)
2. **Scrivi 3 hook alternativi** con meccanismi diversi e scegli il migliore.
3. **Scrivi il post** seguendo la struttura scelta.
4. **Passa la checklist** di `guide/08-checklist-qualita.md` e correggi.
5. **Decidi il visual** con la tabella del file `07`. Se serve, scrivi il prompt completo partendo dal template.
6. **Scrivi il primo commento** (facoltativo): un approfondimento, una domanda o un link, mai un "link in bio".

## Formato dell'output (sempre questo)
```markdown
# [Titolo interno del post]

**Brief** — Target: … · Leva: … · Struttura: … · Obiettivo: …

## Hook alternativi
1. …
2. …
3. …

## Post
[testo pronto da incollare]

## Visual
Tipo: [nessuno | metafora | card trascrizione | tipografica | carosello | meme | foto reale]
Prompt:
[prompt completo, pronto da incollare nel generatore]
(oppure: "Nessun visual: testo semplice.")

## Primo commento (facoltativo)
…

## Checklist
[punteggio x/15 e i punti mancati]
```

Salva ogni post generato in `post/AAAA-MM-GG-slug.md`.

## Regole non negoziabili
- **Mai inventare** numeri, statistiche, clienti, testimonianze o citazioni. Se manca un dato, costruisci il post su un episodio o su un ragionamento, e segnala `[DATO DA INSERIRE]`.
- Claim pubblici utilizzabili: solo quelli della tabella del file `03`, citati come "dati interni Aiclo".
- Mai parlare male dei venditori, mai nominare i concorrenti, mai usare la paura del licenziamento come leva.
- Mai presentare Aiclo come uno strumento di controllo.
- In italiano. Niente parole vietate (file `05`).
