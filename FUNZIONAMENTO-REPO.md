# Come funziona la repo `aiclo-post-generator`

Documento di passaggio per un assistente AI (es. GrokBot) che deve usare questa repo per scrivere post LinkedIn. Riassume struttura, procedura e regole. In caso di dubbio valgono i file originali citati, in particolare `CLAUDE.md`, che è la fonte delle istruzioni operative.

---

## 1. Che cos'è

È una **macchina per scrivere post LinkedIn** in italiano, fatta solo di file Markdown (niente codice da eseguire). I post escono dai **profili personali** del team di **Aiclo**, una piattaforma di conversation intelligence per i team di vendita delle PMI italiane: registra e trascrive le trattative e le valuta con l'AI.

- **Obiettivo unico: engagement** (reazioni, commenti, condivisioni). Non si vendono demo.
- Il post deve valere anche per chi non comprerà mai Aiclo.
- **Pubblico:** manager commerciali (titolari-manager, manager promossi) e venditori delle PMI italiane.
- **Autori attuali:** Andrea Aureli (CEO, visione e numeri aggregati), Damiano Aureli (Co-founder, angolo da confermare), Simone Continenza (Head of Sales, campo, trattative e coaching).
- **Quantità:** a richiesta. Se si chiedono più post insieme, si variano autore, target e struttura.

Esempi di richiesta:
> "Scrivimi un post per Simone sui venditori che non fanno follow-up."
> "Dammi 3 post per Andrea, uno per manager e due per venditori, strutture diverse."

---

## 2. Mappa dei file

| Percorso | Cosa contiene | Quando si legge |
|----------|---------------|-----------------|
| `CLAUDE.md` | Istruzioni operative: procedura, formato di output, regole non negoziabili | Sempre, per primo |
| `post/<autore>/profilo.md` | Chi firma: ruolo, voce, espressioni, temi, storie vere | **Obbligatorio** |
| `post/<autore>/post-pubblicati.md` | Post già usciti, per calibrare la voce | Se esiste |
| `post/<autore>/AAAA-MM-GG-slug.md` | Post generati (output) | Gli ultimi 5, per non ripetersi |
| `post/README.md` | Tabella autori e regole di distribuzione | Per scegliere l'autore |
| `post/_template-autore/` | Modello per aggiungere un autore | Solo per nuovi autori |
| `guide/01-analisi-post-benchmark.md` | 18 post di riferimento analizzati, 7 categorie | Per approfondire |
| `guide/02-anatomia-post-vincente.md` | **Le 11 leggi e le 7 strutture (S1-S7)**, mix editoriale | **Obbligatorio** |
| `guide/03-icp-aiclo.md` | Il prodotto, i **claim pubblici utilizzabili**, l'ICP, le obiezioni | Per numeri e prodotto |
| `guide/04a-manager.md` | Mappa dell'empatia del manager, paure, leve emotive | **Obbligatorio** se target Manager |
| `guide/04b-venditore.md` | Mappa dell'empatia del venditore, i 4 tipi, leve emotive | **Obbligatorio** se target Venditore |
| `guide/04c-scontro-e-terreno-comune.md` | Manager vs venditore: le due letture, il terreno comune | **Obbligatorio** |
| `guide/05-tono-di-voce.md` | Tono, lessico, **parole vietate**, formattazione | **Obbligatorio** |
| `guide/06-hook-e-chiusure.md` | 8 meccanismi di hook, 5 chiusure, **6 leve per i commenti** | Sempre |
| `guide/07-prompt-grafiche.md` | Quando serve una visual, 12 regole, brand, template A-L dei prompt | Se serve una visual |
| `guide/08-checklist-qualita.md` | Checklist da 19 punti prima di pubblicare | Sempre, alla fine |
| `guide/09-banca-spunti.md` | Aperture pronte per manager, venditori, entrambi | Per idee |
| `dati/insight-trattative.md` | Numeri aggregati reali (**solo righe `Approvato: sì`**) | Per numeri "da analisi Aiclo" |
| `dati/episodi-trattative.md` | Scene di trattative anonimizzate | Spunti per S4 |
| `dati/clienti-e-risultati.md` | Casi di prima e dopo | Spunti |
| `ricerca/profilo-target.md` | Profilo psicologico del target con fonti | Per approfondire |
| `ricerca/risultati-test.md` | Esiti dei test A/B sulle ipotesi | Per aggiornare le guide |
| `brand/logo-bianco.png`, `brand/logo-nero.png` | Logo da sovrapporre alle grafiche | Per le visual |
| `esempi/` | 3 post d'esempio completi | Come riferimento di formato |
| `domande-aperte.md` | Decisioni prese e cose che mancano | Per contesto |

---

## 3. Procedura per scrivere un post

1. **Autore.** Se l'utente non lo indica, chiederlo. Leggere `profilo.md` e gli ultimi 5 post nella sua cartella per non ripetere temi, hook o strutture.
2. **Brief.** Se l'utente non lo dà, sceglierlo e scriverlo in testa all'output:
   - **Target:** Manager | Venditore | Entrambi. Alternarli: scegliere quello meno usato di recente dall'autore (mai più di 2 post di fila sullo stesso target).
   - **Sotto-target** (facoltativo): titolare-manager, manager promosso, oppure uno dei 4 venditori (fuoriclasse, chi sta crescendo, veterano sul campo, chi è in difficoltà).
   - **Leva emotiva:** dalle tabelle di `04a`/`04b`/`04c`.
   - **Leva per i commenti:** una delle 6 del file `06` (vedi §5).
   - **Struttura:** S1-S7 o Meme (vedi §4).
   - **Obiettivo:** commenti | condivisioni | salvataggi.
   - **Materiale reale:** un insight, un episodio o un cliente da `dati/`.
3. **Scrivere 3 hook alternativi** con meccanismi diversi e scegliere il migliore, spiegando perché.
4. **Scrivere il post** con la struttura scelta e la voce dell'autore.
5. **Passare la checklist** di `guide/08` e correggere.
6. **Decidere la visual** con la tabella del file `07`, rispettando le 12 regole. Alternare i tipi: mai tre post di fila con la stessa card scura.
7. **Salvare** in `post/<autore>/AAAA-MM-GG-slug.md`. Se si usa una riga di `dati/`, scrivere il nome del post nella colonna "Usato in".

---

## 4. Le regole di scrittura (sintesi del file `02`)

### Le 11 leggi
1. Prima riga: una scena, un numero o un'accusa, max 12-15 parole. Deve reggersi da sola prima del "…altro".
2. Un nemico: una credenza, un'abitudine, uno status quo. Mai un concorrente, mai il cliente.
3. Pelle in gioco: prima persona, da chi ha visto le trattative.
4. Un numero o dettaglio concreto ogni 80-100 parole (dispari e precisi battono i tondi).
5. Un'idea sola.
6. Dare un nome alla cosa (un concetto ripetibile).
7. Prosa breve, a capo spesso; liste solo numerate e di 3-5 voci.
8. 150-300 parole (sotto 100 solo meme o provocazioni secche).
9. Chiusura in una frase, citabile.
10. Il prodotto al massimo è una comparsa (vedi regole).
11. Il commento deve far fare bella figura a chi lo scrive.

### Le 7 strutture
| Codice | Nome | Schema in breve | Obiettivo tipico |
|--------|------|-----------------|------------------|
| S1 | Ribaltamento | Caso che smentisce una credenza → perché è sbagliata → cosa fare → frase che ribalta | Commenti |
| S2 | Concetto con un nome | Nome + storiella → 3 conseguenze → perché oggi è peggio → cosa fare | Condivisioni |
| S3 | Confessione da manager | Errore fatto → cosa credevo → cosa mi ha fatto cambiare idea → nuovo criterio | Commenti dei manager |
| S4 | Dentro la trattativa | Minuto X, cosa dice il cliente → risposta del venditore → esito → lezione | Autorevolezza |
| S5 | Storia dal campo | Scena personale → caduta → svolta → numeri dopo → frase umana | Fiducia |
| S6 | Formula / strumento | Problema settimanale → formula max 5 passi → esempio → errore tipico | Salvataggi |
| S7 | Due versioni | Stessa cosa letta da manager e venditore, con rispetto → dove hanno ragione entrambi → domanda che divide | Commenti da entrambi |
| Meme | Provocazione secca | Breve, ironica | Reach verso i venditori |

Mix consigliato su 10 post: S1 ×2, S2 ×1, S3 ×1, S4 ×2, S5 ×1, S6 ×1, S7 ×2, Meme bonus.

### Tono e forma (file `05`)
- Riga 1 il gancio, riga 2 vuota, paragrafi di 1-3 righe.
- Emoji: zero o una, mai in apertura. Hashtag: zero o max 3 in fondo. **Mai link nel corpo** (eventualmente nel primo commento).
- **Parole vietate:** insight, data-driven, enablement, revenue intelligence, conversation intelligence (nei post), leverage, rivoluzionario, game changer, nel panorama odierno, in un mondo in cui, sfida, viaggio, potenziare, sbloccare, ecosistema, sinergia, a 360°, fondamentale, cruciale, "ecco perché" come apertura, "Spoiler:", "Plot twist:", "Facciamo un passo indietro".
- Italiano "da campo", poco gergo inglese.

---

## 5. Le 6 leve per i commenti (file `06`)
Chi commenta deve uscirne bene: **mai chiedere confessioni in prima persona.**

| Leva | Esempio |
|------|---------|
| Schierarsi | "Registreresti tutte le trattative del tuo team? Sì o no, e perché." |
| Difesa dell'identità | "«Ha talento» è la spiegazione più comoda che un'azienda possa darsi." |
| Racconto di guerra | "Qual è la scusa più creativa che hai sentito dopo una trattativa persa?" |
| "Parla di me" | "Il lunedì chiedi com'è andata. Ti raccontano una versione. Da lì decidi." |
| Nemico comune | "Il CRM compilato alle dieci di sera, in macchina, per qualcuno che non lo leggerà." |
| Confessione spostata | "Il feedback più inutile che ti abbia dato un capo. Comincio io." |

---

## 6. Regole non negoziabili

**Storie e numeri**
- **Le storie si possono costruire** (prima e dopo, scene di trattativa, clienti tipo, frasi di manager e venditori), purché verosimili, **anonime** e coerenti con i clienti tipici del file `03`. Nell'output: `storia costruita`.
- **I numeri si possono costruire** se presentati come esperienza dell'autore, come esempio o dentro una storia. Nell'output: `numero costruito`.
- **Unico limite:** un numero presentato come *risultato dell'analisi di Aiclo* ("nelle 10.000 trattative che abbiamo analizzato, il X%…") viene **solo** dai claim del file `03` o dalle righe con `Approvato: sì` in `dati/insight-trattative.md`.
- Il dato **"63% delle vendite sul territorio" non si usa**: non ha fonte.
- Il **5%** (un manager ascolta in media il 5% delle trattative) si cita come dato interno ("nei team che seguiamo"), non come statistica di mercato.
- Mai citazioni inventate attribuite a persone reali con nome.

**Prodotto**
- Aiclo **quasi mai nominato**: al massimo 1 post su 8, una sola volta, mai nella prima riga.
- Test pubblicità: se togli il nome Aiclo il post deve valere ancora.
- Mai nominare i concorrenti. Mai presentare Aiclo come strumento di controllo.
- I clienti si citano solo come previsto in `dati/clienti-e-risultati.md`.

**Tono**
- Si provoca un pensiero, **mai una persona**. Niente attacchi, niente presunzione, niente "io ho capito e voi no".
- Mai scrivere che i venditori mentono; le scorciatoie solo con ironia.
- Mai usare la paura del licenziamento come leva.
- Nessuna affermazione legale (Statuto dei lavoratori, privacy, consenso) senza un legale.
- Le paure etichettate **Ipotesi** si usano come scena o domanda, mai come verità generale.

---

## 7. Formato dell'output (sempre questo)

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

Un esempio reale completo è `post/simone-continenza/2026-11-09-implicazioni-1-5.md`; altri in `esempi/`.

---

## 8. Visual (file `07`)

- **Formato:** sempre verticale 4:5, 1080×1350, anche per i caroselli.
- **Brand:** accento ambra **#F9A517** (sempre presente, su un solo elemento); rosso dati #EE293A solo per un errore; verde #7BD1A0 e blu #8FB8F0 solo per punteggi e grafici. Font: Sora (titoli), DM Sans (testo), IBM Plex Mono (etichette e numeri). Sfondo quasi nero **non** obbligatorio: alternare con carta crema, bianco sporco, foto vere.
- **Logo:** mai generato dall'AI. Nel prompt chiedere di lasciare libero l'angolo in basso a destra, poi sovrapporre `brand/logo-bianco.png` o `brand/logo-nero.png` (circa 15% della larghezza, margine 48px).
- **Regole chiave:** un solo protagonista grande almeno metà immagine; un'anomalia che ferma il pollice; max 8 parole; imperfetto batte patinato; un solo colore che urla.
- **Vietati:** strette di mano, grafici che salgono, robot, cervelli luminosi, persone che indicano schermi, gradienti viola-blu, 3D lucido, emoji nell'immagine, mappe mentali.
- **Template disponibili:** A metafora (S2), B card trascrizione (S4), C tipografica (S1), D carosello (S6), E meme, F screenshot della piattaforma con dati demo, G oggetto reale, H numero gigante, I grafico che fa male, J chat del cliente, K scritto a mano, L foto vera dell'autore (da scattare).

---

## 9. Checklist finale (file `08`)
Si pubblica solo con **almeno 17 sì su 19**; i punti ⛔ sono obbligatori:
- ⛔ Una sola idea.
- ⛔ Numeri attribuiti ad Aiclo reali; quelli costruiti segnalati.
- ⛔ Storie costruite verosimili, anonime e segnalate.
- ⛔ Chi commenta ne esce bene; nessuna affermazione legale.
- ⛔ Aiclo nominato al massimo una volta, mai nella prima riga.
- ⛔ Provoca un pensiero, non attacca nessuno.

Gli altri punti riguardano gancio (<15 parole), nemico chiaro, densità di numeri, target chiaro nelle prime 3 righe, leva dell'empatia, lunghezza, paragrafi brevi, emoji, nessun link, chiusura citabile, voce dell'autore. Test finali: **WhatsApp** (un venditore lo girerebbe a un collega?), **titolare** (un manager lo metterebbe nella chat del team?), **pubblicità** (vale anche senza il nome Aiclo?).

---

## 10. Regole di distribuzione tra autori (`post/README.md`)
- Lo stesso tema non esce da due autori nella stessa settimana.
- Ogni autore alterna post per manager e per venditori.
- Il tema va all'autore con l'angolo più credibile (trattativa vissuta → Simone; numeri aggregati di mercato → Andrea).

## 11. Manutenzione
- **Nuovo autore:** copiare `post/_template-autore/` in `post/nome-cognome/`, compilare `profilo.md`, aggiungere la riga in `post/README.md`.
- **Nuovi dati:** aggiungere righe in `dati/`; un numero diventa citabile come "analisi Aiclo" solo con `Approvato: sì`.
- **Test A/B:** annotare i risultati in `ricerca/risultati-test.md` e aggiornare le etichette Ipotesi → Verificata / Smentita nelle guide.
- **Cose ancora aperte:** vedi `domande-aperte.md` (profili autori da completare, angolo di Damiano, generatore di immagini da scegliere, episodi reali da raccogliere).
