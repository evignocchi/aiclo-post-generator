# Istruzioni per generare i post LinkedIn di Aiclo

Questa repository è una **macchina per scrivere post LinkedIn** che escono dai **profili personali** del team Aiclo (conversation intelligence per i team di vendita delle PMI italiane).

**Obiettivo unico: engagement** (reazioni, commenti, condivisioni). Non si vendono demo. Il post deve valere anche per chi non comprerà mai Aiclo.

## Prima di scrivere, leggi
0. `guide/00-stile-di-scrittura.md`: il documento unico sullo stile (target incrociato con lo stile, voci, regole anti-AI, i due registri, gli appunti dal campo) **(obbligatorio)**
1. `post/<autore>/profilo.md` (e `post-pubblicati.md`, se c'è): chi firma il post, la sua voce, i suoi temi **(obbligatorio)**
2. `guide/02-anatomia-post-vincente.md`: le 11 leggi e le 7 strutture **(obbligatorio)**
3. `guide/04a-manager.md` o `guide/04b-venditore.md` (a seconda del target) e `guide/04c-scontro-e-terreno-comune.md`: a chi parli, quale nervo tocchi, come far commentare **(obbligatorio)**
4. `guide/05-tono-di-voce.md`: come parli e fin dove si può provocare **(obbligatorio)**
5. `guide/06-hook-e-chiusure.md` e `guide/09-banca-spunti.md`: aperture, chiusure, leve per i commenti e spunti pronti
6. `dati/`: insight aggregati (solo le righe con `Approvato: sì`), episodi e clienti da usare come spunto
7. `guide/03-icp-aiclo.md`: il prodotto e i claim pubblici
8. `guide/07-prompt-grafiche.md`: brand e prompt, solo se il post richiede un visual
9. `guide/01-analisi-post-benchmark.md` e `ricerca/profilo-target.md`: per approfondire perché le regole sono queste

## Procedura
1. **Autore.** Se l'utente non lo indica, chiedilo. Leggi il suo `profilo.md` e gli ultimi 5 post nella sua cartella, per non ripetere temi, hook o strutture.
2. **Brief** (se l'utente non lo dà, sceglilo tu e scrivilo in testa all'output):
   - Target: Manager | Venditore | Entrambi. **Alternali**: guarda gli ultimi post dell'autore e scegli il target meno usato di recente.
   - Sotto-target (facoltativo): titolare-manager, manager promosso, oppure uno dei 4 venditori (fuoriclasse, chi sta crescendo, veterano sul campo, chi è in difficoltà)
   - Leva emotiva (dalle tabelle dei file `04a`/`04b`/`04c`)
   - Leva per i commenti (una delle 6 del file `06`)
   - Registro: post costruito (S1-S7 o Meme, 150-300 parole) oppure appunto dal campo (formati A-G, 50-150 parole). Alternali più o meno a metà
   - Obiettivo: commenti | condivisioni | salvataggi
   - Materiale reale: insight, episodio o cliente dalla cartella `dati/`
3. **Scrivi 3 hook alternativi** con meccanismi diversi e scegli il migliore.
4. **Scrivi il post** con la struttura scelta e la voce dell'autore.
5. **Passa la checklist** di `guide/08-checklist-qualita.md` e correggi.
6. **Decidi il visual** con la tabella del file `07` e rispetta **le 12 regole per una visual che ferma lo scroll** (stesso file). Se serve, scrivi il prompt completo partendo dal template e usando i colori del brand. Alterna i tipi: mai tre post di fila con la stessa card scura.
7. **Salva** in `post/<autore>/AAAA-MM-GG-slug.md`.

Quantità: **a richiesta**. Se vengono chiesti più post insieme, variare autore, target e struttura.

## Formato dell'output (sempre questo)
```markdown
# [Titolo interno del post]

**Autore** — … · **Brief** — Target: … · Leva: … · Leva commenti: … · Struttura: … · Obiettivo: …
**Fonti dati** — [riga di dati/… usata, "storia costruita", "numero costruito", oppure "nessuna"]

## Hook alternativi
1. …
2. …
3. …

## Post
[testo pronto da incollare]

## Visual
Tipo: [nessuno | oggetto reale | numero gigante | grafico che fa male | chat | scritto a mano | foto dell'autore | metafora | card trascrizione | tipografica | carosello | meme | screenshot]
Prompt:
[prompt completo, pronto da incollare nel generatore]
Anomalia: [cosa c'è di storto o di strano che ferma il pollice, in una riga]
(oppure: "Nessun visual: testo semplice.")

## Primo commento (facoltativo)
…

## Checklist
[punteggio x/19 e i punti mancati]
```

## Regole non negoziabili
- **Le storie si possono costruire.** Prima e dopo, scene di trattativa, clienti tipo, frasi di manager e venditori: si possono inventare, purché siano verosimili, anonime (mai un'azienda o una persona reale con il nome) e coerenti con il prodotto e con i clienti tipici del file `03`. I numeri dentro una singola storia (il tasso di chiusura di un venditore, il minuto di una trattativa) si possono costruire. Nell'output, alla voce **Fonti dati**, scrivi `storia costruita`, così l'autore lo sa prima di pubblicare.
- **I numeri si possono costruire**, se sono presentati come esperienza dell'autore ("su 10 'ci penso' che ricevo, ne chiudo 2"), come esempio o dentro una storia. Nell'output, alla voce **Fonti dati**, scrivi `numero costruito`, così l'autore lo verifica con la sua esperienza prima di pubblicare.
- **Unico limite:** un numero presentato come risultato dell'analisi di Aiclo ("nelle 10.000 trattative che abbiamo analizzato, il X%…") viene solo dai claim del file `03` o dalle righe approvate in `dati/`. Mai citazioni inventate attribuite a persone reali con il nome.
- **Il dato "63% delle vendite sul territorio" non si usa**: non ha una fonte.
- **Aiclo in circa 1 post su 4**: l'obiettivo principale è l'engagement, il secondo è far capire cosa risolve Aiclo. Quando c'è, è nominato una sola volta, mai nella prima riga, dentro la storia (dato, uso personale, perché l'abbiamo costruito, caso cliente, PS), mai con elenchi di funzionalità (vedi `guide/00-stile-di-scrittura.md`, sezione 1). La storia di fondazione di Aiclo non si inventa mai.
- **Parolacce**: quasi mai; al massimo una leggera in uno sfogo, un post su dieci.
- **Foto vere**: non si generano. Se il post ne ha bisogno, sotto il post si scrive la mail di richiesta all'autore (template in `guide/00-stile-di-scrittura.md`, sezione 6.3).
- **Si provoca un pensiero, mai una persona.** Niente attacchi, niente presunzione, niente tono da "io ho capito e voi no" (vedi il file `05`).
- **Chi commenta deve uscirne bene**: mai chiedere confessioni in prima persona, usare la confessione spostata.
- **Mai scrivere che i venditori mentono**; le scorciatoie solo con ironia.
- **Nessuna affermazione legale** (Statuto dei lavoratori, privacy, consenso) senza revisione di un legale.
- Le paure etichettate **Ipotesi** si usano come scena o domanda, mai come verità generale. Le frasi ricostruite dei file `04a`/`04b` si possono usare dentro una storia costruita, mai attribuite a una persona reale.
- Il 5% si cita come dato interno Aiclo ("nei team che seguiamo"), non come statistica di mercato.
- Mai nominare i concorrenti, mai usare la paura del licenziamento come leva, mai presentare Aiclo come uno strumento di controllo.
- I clienti si citano solo come previsto in `dati/clienti-e-risultati.md`.
- In italiano. Niente parole vietate (file `05`).

## Aggiungere un autore
Copia `post/_template-autore/` in `post/nome-cognome/`, compila `profilo.md` e aggiungi l'autore alla tabella in `post/README.md`.
