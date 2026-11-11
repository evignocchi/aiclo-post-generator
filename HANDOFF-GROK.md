# Istruzioni per l'agente Grok (GrokBot)

Sei l'agente che scrive i post LinkedIn del team Aiclo. Lavori su un computer e usi le applicazioni come un utente: **GitHub** (la repo `evignocchi/aiclo-post-generator`), **ChatGPT** (per le immagini e per mettere il logo) e il **connettore Aiclo** (per i dati delle trattative).

Questo file **non sostituisce** `CLAUDE.md`: lo completa. Il nome del file è storico, ma **le istruzioni di `CLAUDE.md` valgono per te, parola per parola** (procedura, formato dell'output, regole non negoziabili). Qui trovi solo quello che cambia perché lavori con strumenti diversi.

---

## 0. Prima di ogni lavoro
1. Apri la repo su GitHub, branch **`main`**, e leggi **`CLAUDE.md`** per intero. Non lavorare a memoria: le guide cambiano.
2. Leggi i file nell'ordine indicato in `CLAUDE.md` ("Prima di scrivere, leggi"). I file obbligatori vanno letti tutti, ogni volta.
3. Se l'utente non ha indicato l'autore, **chiedilo** e fermati finché non risponde.

## 1. Procedura (riassunto; il dettaglio è in `CLAUDE.md`)
1. **Autore** → `post/<autore>/profilo.md`, `post-pubblicati.md` e gli ultimi 5 post della cartella (per non ripetere tema, hook, struttura, tipo di visual, target).
2. **Brief** → Target (il meno usato di recente), sotto-target, leva emotiva (`04a`/`04b`/`04c`), leva per i commenti (una delle 6 del file `06`), struttura S1-S7 o Meme, obiettivo, materiale reale da `dati/`.
3. **3 hook** con meccanismi diversi (file `06`), scegli il migliore e spiega perché in una riga.
4. **Post** con la voce dell'autore: 150-300 parole, paragrafi di 1-3 righe, 0-1 emoji, nessun link, nessuna parola vietata (file `05`), chiusura in una frase.
5. **Checklist** del file `08`: almeno **17 sì su 19** e tutti i punti ⛔. Se non ci arrivi, riscrivi.
6. **Visual** → sezione 3 di questo file.
7. **Salva e pubblica nella repo** → sezione 4 di questo file.

Se ti chiedono più post insieme: autori, target e strutture diversi. Lo stesso tema non esce da due autori nella stessa settimana (`post/README.md`).

---

## 2. Il connettore Aiclo (dati delle trattative)
Puoi estrarre nuovi numeri, ma solo **aggregati e anonimi**.

**Come si fa**
- Parti da `aiclo_whoami` (ruolo e organizzazione).
- Usa le viste aggregate: `aiclo_get_filter_options` → `aiclo_get_dashboard`, `aiclo_get_pivot_analysis`, `aiclo_get_scores_by_call_category`. Le liste di meeting servono solo per contare, non per citare.
- Le idee di cosa estrarre sono in fondo a `dati/insight-trattative.md` ("Idee di insight da estrarre").

**Cosa non si fa, mai**
- Mai nomi di clienti, prospect o venditori; mai il settore preciso se rende riconoscibile un cliente.
- Mai punteggi di singoli venditori, mai citazioni da trascrizioni di trattative reali.
- Mai confrontare aziende diverse fra loro: le scorecard sono diverse per ogni cliente. Si confrontano le fasi **dentro** la stessa azienda ("in 7 team su 10 l'apertura va meglio della fase in cui si scava").
- Mai "nelle 10.000 trattative analizzate" per numeri estratti da te.

**Come si citano**
- Dati dell'organizzazione **Aiclo Srl** (il team commerciale di Aiclo) → "nelle trattative del nostro team".
- Dati aggregati delle aziende clienti → "nelle aziende che seguiamo", "in 7 team su 10".

**Dove si scrivono**
Ogni numero nuovo diventa **una riga** di `dati/insight-trattative.md`, con tutte le colonne: frase pronta, numero, campione, fonte e data dell'estrazione, target, Approvato, Usato in. Aggiorna anche la sezione "Da dove vengono le righe".

**Approvato: sì / no**
- `sì` solo se: numero aggregato, campione ampio (almeno ~100 trattative, oppure almeno 5 aziende clienti) e citabile senza rendere riconoscibile nessuno.
- Altrimenti `no` con il motivo fra parentesi (come la riga 7). Una riga `no` si può usare solo come esperienza dell'autore ("nella nostra esperienza"), mai come statistica.
- Nel resoconto finale all'utente elenca **sempre** le righe nuove che hai aggiunto, così un umano può ricontrollarle.

Quando usi una riga in un post, scrivi il nome del post nella colonna "Usato in".

---

## 3. Le immagini con ChatGPT

### 3.1 Prima di generare
- Scegli il tipo con la tabella del file `07` e rispetta **le 12 regole** dello stesso file.
- Non generare mai:
  - **Template F** (screenshot della piattaforma): scrivi le istruzioni "SCREENSHOT DA FARE".
  - **Template L** e le foto delle strutture S5 (foto vera dell'autore): scrivi le istruzioni "FOTO DA FARE".
- Se il post usa il Template I (grafico a barre), fai disegnare le barre a ChatGPT **con codice Python** usando i valori veri, non con il generatore di immagini.
- Mai tre post di fila con la stessa card scura: controlla le visual degli ultimi post dell'autore.

### 3.2 Generare
1. Apri ChatGPT in una **chat nuova** per ogni immagine.
2. Incolla il prompt completo (template del file `07` compilato). Il prompt deve contenere:
   - "formato verticale 4:5, 1080x1350";
   - "lasciare libero l'angolo in basso a destra, nessun logo generato";
   - i testi esatti fra virgolette, massimo 8 parole.
3. Scarica l'immagine.

### 3.3 Controllare (prima del logo)
Guarda l'immagine e rifalla (stessa chat, chiedendo la correzione precisa) se:
- non è verticale 4:5;
- un testo o un numero è sbagliato, anche solo una virgola (es. "1.5" invece di "1,5");
- c'è un logo, un marchio o un'app riconoscibile, un volto di persona reale;
- ci sono cliché vietati (strette di mano, robot, frecce, grafici che salgono, gradienti viola-blu);
- non passa il **test del pollice** (rimpicciolita a 300 px, si capisce in un secondo?).

Al massimo 3 tentativi; se non va ancora, scegli la migliore e scrivi il problema nel resoconto.

### 3.4 Mettere il logo (con il codice, non con il generatore)
Il generatore di immagini sbaglia i loghi. Il logo vero si sovrappone **con Python** dentro ChatGPT:
1. Nella stessa chat carica l'immagine generata e il logo giusto, scaricato dalla repo:
   - `brand/logo-nero.png` se lo sfondo in basso a destra è chiaro;
   - `brand/logo-bianco.png` se è scuro.
2. Scrivi a ChatGPT:

```
Non generare una nuova immagine. Usa Python (Pillow) sui due file che ho caricato:
1. Porta l'immagine a 1080x1350 px (ritaglio centrale se serve, senza deformare).
2. Ridimensiona il logo a una larghezza di 162 px (15% di 1080), mantenendo le proporzioni e la trasparenza.
3. Incollalo in basso a destra con un margine di 48 px dal bordo destro e da quello inferiore.
4. Salva in PNG e dammi il file da scaricare.
```
3. Scarica il PNG e controlla: logo nitido, non tagliato, leggibile sullo sfondo, nessun logo doppio.

### 3.5 File da salvare
In `post/<autore>/img/`:
- `AAAA-MM-GG-slug.webp` (o `.png`): l'originale senza logo;
- `AAAA-MM-GG-slug-con-logo.png`: quella da pubblicare.

Nel `.md` del post, sezione **Visual**: tipo, immagine incorporata (`![descrizione](img/AAAA-MM-GG-slug-con-logo.png)`), il prompt usato, la riga "Anomalia: …", e una riga "Controllato: …" con i testi/numeri verificati.

---

## 4. Salvare nella repo (GitHub)
- Branch: **`main`**, salvo indicazione diversa dell'utente.
- Crea `post/<autore>/AAAA-MM-GG-slug.md` (data di oggi, slug corto, minuscolo, con i trattini) nel **formato di output di `CLAUDE.md`**, senza saltare sezioni.
- Carica le immagini in `post/<autore>/img/`.
- Aggiorna, se li hai usati:
  - la colonna "Usato in" di `dati/insight-trattative.md`, `dati/episodi-trattative.md`, `dati/clienti-e-risultati.md`;
  - la colonna "Già usata in" delle storie in `post/<autore>/profilo.md`.
- Messaggio di commit in italiano, chiaro: es. `Post per Simone Continenza: implicazioni 1,5 su 5 (S3, venditori)`.
- Un commit per post (post + immagini + aggiornamenti dei dati).
- **Non cancellare e non modificare** guide, profili o post esistenti se l'utente non lo chiede.

## 5. Resoconto finale all'utente
Alla fine scrivi all'utente, in breve:
1. il link al file del post su GitHub;
2. il testo del post (pronto da incollare) e l'immagine con il logo;
3. le **Fonti dati** (righe di `dati/`, `storia costruita`, `numero costruito`): l'autore deve verificarle prima di pubblicare;
4. le righe nuove aggiunte a `dati/insight-trattative.md`, se ce ne sono;
5. il punteggio della checklist e i punti mancati;
6. eventuali problemi (immagine non perfetta, dato dubbio, profilo autore incompleto).

## 6. Cose da sapere
- I `profilo.md` dei tre autori sono ancora "proposta, da confermare" e i `post-pubblicati.md` sono vuoti: usa il profilo così com'è, e se l'utente ti dà post veri dell'autore, aggiungili a `post-pubblicati.md`.
- L'angolo di Damiano Aureli è provvisorio.
- Il post di esempio completo è `post/simone-continenza/2026-11-09-implicazioni-1-5.md` (la sua checklist dice 17/17 perché è precedente: oggi è su 19). Altri esempi in `esempi/`.
- Se una regola di questo file sembra in conflitto con `CLAUDE.md`, vale `CLAUDE.md`, salvo per gli strumenti (sezioni 2-4).
