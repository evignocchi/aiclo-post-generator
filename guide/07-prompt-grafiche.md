# 07 — Grafiche: quando servono e i prompt per generarle

## Quando mettere una grafica
Dai post di riferimento: i vincenti sono **testo semplice** oppure hanno **un video nativo** (#16, #4) o **un'immagine metafora** (#17, #9). Le infografiche-lista non compaiono fra i vincenti.

| Struttura del post | Prima scelta | Alternativa |
|--------------------|--------------|-------------|
| S1 Ribaltamento | **Numero gigante** (Template H) o **scritto a mano** (Template K) | Card tipografica (Template C) |
| S2 Concetto con nome | **Oggetto reale del mestiere** (Template G) o metafora (Template A) | Scritto a mano con il nome del concetto |
| S3 Confessione | **Foto vera dell'autore** (Template L) | Scritto a mano (Template K) |
| S4 Dentro la trattativa | **Chat / messaggio del cliente** (Template J) o screenshot reale (Template F) | Card trascrizione (Template B) |
| S5 Storia dal campo | **Foto vera** (mai generata) | Oggetto reale (Template G) |
| S6 Formula / strumento | **Carosello** (Template D) con copertina forte | Grafico che fa male (Template I) |
| Meme | Immagine meme (Template E) | — |
| Post con un dato forte | **Grafico che fa male** (Template I) o numero gigante (Template H) | — |

## Le 12 regole per una visual che ferma lo scroll
La visual ha un solo compito: **fermare il pollice**. Se non ferma il pollice, meglio il testo semplice.

1. **Test del pollice.** Rimpicciolita a 300 pixel (come nel feed sul telefono), in un secondo si capisce cosa c'è. Se bisogna leggere per capire, è sbagliata.
2. **Un solo protagonista, grande.** L'elemento principale occupa almeno metà dell'immagine. Niente composizioni "equilibrate" con tre cose piccole.
3. **Tensione, non decorazione.** La visual mostra un'anomalia, un contrasto o un errore: la barra corta fra quelle lunghe, il numero cerchiato in rosso, il post-it con "ci penso" sul preventivo, la sedia vuota al tavolo della trattativa.
4. **Concreto batte astratto.** Oggetti veri del mestiere: preventivo stropicciato, cruscotto con il tablet, CRM pieno di note, telefono con 9 chiamate perse, lavagna della riunione del lunedì. Mai icone, frecce, ingranaggi, cervelli, lampadine, razzi.
5. **Persone vere.** Un volto (anche di spalle, tagliato, in controluce) batte qualsiasi grafica. La foto vera dell'autore batte quella generata. Mai la gente sorridente da banca d'immagini.
6. **Il numero diventa forma.** Un dato non si elenca: si disegna. Un 1,5 enorme, una barra che si ferma a metà, 7 omini su 10 colorati.
7. **Poco testo, enorme.** Massimo 8 parole, il testo principale alto almeno un decimo dell'immagine. E deve **aggiungere** qualcosa alla prima riga del post, non ripeterla.
8. **Imperfetto batte patinato.** Scritto a mano, foto col telefono, screenshot vero, post-it, lavagna, foglio a quadretti. LinkedIn è pieno di grafiche perfette: la mano umana si nota.
9. **Il brand è un accento, non una gabbia.** L'ambra #F9A517 è il segno riconoscibile e c'è sempre (un cerchio, una parola, una barra). Lo sfondo quasi nero **non** è obbligatorio: si alterna con carta, bianco sporco, foto vere. Mai tre post di fila con la stessa card scura.
10. **Un colore che urla, uno solo.** Ambra (o il rosso dati #EE293A per un errore) su un'immagine altrimenti neutra. Due colori che urlano si annullano.
11. **Sempre verticale 4:5** (1080x1350), anche per i caroselli: occupa più spazio nel feed.
12. **Niente cliché.** Vietati: strette di mano, grafici che salgono, robot, cervelli luminosi, persone che indicano uno schermo, gradienti viola-blu, 3D lucido, emoji dentro l'immagine, mappe mentali.

### Le 3 domande prima di scrivere il prompt
1. **Cosa vede il pollice** in un secondo?
2. **Qual è l'anomalia** (cosa c'è di storto, di strano, di sbagliato)?
3. **Si capisce anche senza il post?** Se sì, è buona. Se no, rinforzare il protagonista o tagliare.

Nell'output, sotto il prompt, scrivere in una riga la risposta alla domanda 2 ("Anomalia: …").

## Brand (estratto dal CSS di aiclo.io)
Il sito è **dark**: sfondo quasi nero, testo bianco, un solo colore d'accento ambra/arancio.

```
SFONDO          = #08090B   (quasi nero; varianti per le card: #0E1014, #101318, #181C24)
SUPERFICIE      = #262E36   (bordi e pannelli)
TESTO           = #FFFFFF   (secondario: #9CA3AF)
ACCENTO         = #F9A517   (ambra Aiclo, il colore del brand; usarlo per 1 parola o 1 elemento)
ACCENTO CHIARO  = #FAD394   (velatura: ambra al 12% sullo sfondo)
COLORI DATI     = verde #7BD1A0 · blu #8FB8F0 · rosso #EE293A   (solo per punteggi e grafici)
FONT TITOLI     = Sora (bold)
FONT TESTO      = DM Sans
FONT DATI/LABEL = IBM Plex Mono (etichette tipo "CLIENTE · 23:14", numeri)
LOGO            = simbolo (occhio stilizzato: un cerchio pieno dentro un rombo aperto a chevron)
                  + wordmark minuscolo "aiclo" in sans-serif geometrica bold.
                  File: brand/logo-bianco.png (su sfondo scuro), brand/logo-nero.png (su sfondo chiaro)
FORMATO         = 1080x1350 (4:5) sempre, anche per i caroselli
```

### Logo nelle grafiche
I generatori di immagini **sbagliano i loghi**. Regola: nel prompt chiedere sempre **"lascia libero l'angolo in basso a destra, nessun logo"** e poi **sovrapporre il PNG vero** (`brand/logo-bianco.png` o `brand/logo-nero.png`) in Canva/Figma, largo circa il 15% della grafica, con un margine di 48px.
Nei template qui sotto è già scritto così: "spazio vuoto per il logo (nessun logo generato)".

Regola: **sfondo scuro + bianco + un tocco di ambra**. Le card chiare si usano solo come eccezione (per esempio una citazione su sfondo `#FEF7E0`).

## Regole valide per ogni prompt
(Oltre alle 12 regole qui sopra.)
- Una sola idea visiva per immagine.
- Massimo 8 parole di testo nell'immagine (i generatori sbagliano le scritte: verificare sempre, e se servono numeri precisi aggiungerli dopo in Canva/Figma).
- Descrivere sempre: inquadratura (primo piano, dall'alto, 3/4), luce (da dove arriva, che colore), materiale (carta, legno, vetro), e cosa è a fuoco.
- Niente stock photo di strette di mano, grafici che salgono o robot.
- Persone realistiche, contesto italiano (auto aziendale, capannone, cucina di un cliente, ufficio di una PMI), mai Silicon Valley.
- Nessun volto riconoscibile di persone reali, nessun logo di terzi.

---

## Template A — Immagine metafora (per S2)
```
Fotografia editoriale concettuale, still life su sfondo quasi nero (#08090B), un'unica luce
laterale calda color ambra (#F9A517) che illumina il soggetto, composizione minimalista.
Soggetto: [OGGETTO ASSURDO CHE RAPPRESENTA IL CONCETTO,
es. "un binocolo con il 95% delle lenti coperto da nastro adesivo nero"].
Stile: realistico, alto contrasto, profondità di campo ridotta.
Nessun testo nell'immagine. Formato 4:5, 1080x1350.
```

## Template B — Card "trascrizione" (per S4)
```
Grafica flat minimalista, sfondo quasi nero #08090B. Al centro una card scura #101318
con bordo sottile #262E36 e angoli arrotondati, stile trascrizione.
In alto nella card un'etichetta in font monospace (IBM Plex Mono), piccola, color ambra #F9A517:
"CLIENTE · 23:14". Sotto, testo grande bianco in font Sora bold:
"[BATTUTA DEL CLIENTE, max 10 parole]".
Più in basso una seconda riga più piccola in grigio #9CA3AF, etichetta monospace "VENDITORE",
testo: "[RISPOSTA DEL VENDITORE, max 8 parole]".
In basso a destra spazio vuoto per il logo (nessun logo generato). Molto spazio vuoto.
Formato 4:5, 1080x1350.
```

## Template C — Card tipografica (per S1 / la chiusura)
```
Poster tipografico minimalista, sfondo quasi nero #08090B, una sola frase centrata
in bianco, font Sora bold molto grande: "[FRASE, max 10 parole]".
Una sola parola in ambra #F9A517. Nessun altro elemento; lasciare vuoto
l'angolo in basso a destra per il logo (nessun logo generato). Formato 4:5, 1080x1350.
```

## Template D — Infografica / slide di carosello (per S6)
```
Slide di carosello LinkedIn, formato 4:5 1080x1350, stile editoriale pulito,
sfondo quasi nero #08090B, titolo in alto in bianco, font Sora bold: "[TITOLO, max 6 parole]".
Contenuto: [N] blocchi numerati in verticale, ognuno con un numero grande in ambra #F9A517
(font IBM Plex Mono) e una riga di testo bianco in DM Sans: 1) "[...]" 2) "[...]" 3) "[...]".
Separatori sottili #262E36, icone lineari sottili, nessuna foto.
Footer in monospace grigio #9CA3AF: "Aiclo · [n]/[totale]". Molto spazio vuoto.
```
Per i caroselli: generare una slide alla volta con lo stesso prompt base e cambiare solo il contenuto. Copertina = hook del post.

## Template E — Meme (per i post meme)
```
Fotografia realistica, stile candid un po' sgranato, [SCENA IRONICA, es. "agente di commercio
italiano di 45 anni in giacca, seduto in una Fiat Panda in un parcheggio industriale al tramonto,
mangia un panino, con un preventivo cartaceo appoggiato sul volante"]. Espressione stanca ma
ironica. Nessun testo nell'immagine (il setup va nel testo del post). Formato 4:5.
```

## Template F — Screenshot reale della piattaforma (✅ autorizzato con dati demo)
Per i post S4 e S6 uno screenshot vero vale più di qualsiasi grafica generata. Istruzioni da scrivere nell'output al posto del prompt:
```
SCREENSHOT DA FARE: [schermata, es. "scorecard di una trattativa di Discovery",
"matrice di coaching", "heatmap del team", "miniscript di un'obiezione"]
- Account demo, nomi fittizi (mai dati di clienti reali)
- Ritaglio stretto sul dettaglio che serve al post, 4:5
- Evidenziare con un riquadro ambra #F9A517 l'elemento di cui parla il post
- Facoltativo: cornice su sfondo #08090B con una riga di titolo in Sora bianco
```
Solo se non è possibile fare lo screenshot, generare un mockup:
```
Mockup di un laptop su una scrivania di legno, schermo con una dashboard SaaS dark
(sfondo #08090B, card #101318, accento ambra #F9A517): matrice 2x2 etichettata
"Star / In crescita / Da supportare / A rischio" con puntini colorati, a fianco una heatmap.
Interfaccia in italiano. Luce naturale, prospettiva 3/4.
```

---

## Template G — Oggetto reale del mestiere (per S2, S5)
```
Fotografia still life realistica, scattata dall'alto o di 3/4, luce naturale laterale da una finestra,
su [SUPERFICIE VERA: scrivania in laminato di un ufficio PMI / cruscotto di un'auto aziendale / tavolo di cucina].
Protagonista, al centro e grande (oltre metà dell'immagine): [OGGETTO CON L'ANOMALIA,
es. "un preventivo stampato e stropicciato con un post-it giallo su cui è scritto a penna 'ci penso'"].
Un solo dettaglio in ambra #F9A517 (es. il post-it, un evidenziatore, una graffetta).
Profondità di campo ridotta, grana leggera, colori naturali, niente look patinato.
Nessun altro testo. Angolo in basso a destra libero per il logo (nessun logo generato). Formato 4:5, 1080x1350.
```

## Template H — Numero gigante (per S1 e post con un dato)
```
Poster minimalista, formato 4:5 1080x1350. Sfondo [carta color crema #F5F0E6 / quasi nero #08090B].
Un solo numero enorme che occupa il 60% dell'altezza: "[NUMERO, es. 1,5]", font Sora extra bold,
colore ambra #F9A517. Sotto, piccolo, in IBM Plex Mono [grigio #6B7280 / #9CA3AF]: "[ETICHETTA, max 6 parole, es. 'su 5. Il nostro voto peggiore']".
Nient'altro. Angolo in basso a destra libero per il logo (nessun logo generato).
```

## Template I — Grafico che fa male (per i post con dati)
```
Grafico a barre orizzontali minimalista, formato 4:5 1080x1350, sfondo [crema #F5F0E6 / quasi nero #08090B].
[N] barre spesse con etichette corte a sinistra in IBM Plex Mono: [ETICHETTA 1 → VALORE], [ETICHETTA 2 → VALORE], ...
Tutte le barre in grigio neutro tranne una: "[ETICHETTA DELL'ANOMALIA]", in ambra #F9A517, visibilmente più corta (o più lunga) delle altre,
con il suo valore scritto grande accanto. Niente assi, niente griglia, niente legenda. Molto spazio vuoto.
Angolo in basso a destra libero per il logo (nessun logo generato).
```
Consiglio: i generatori sbagliano le proporzioni. Meglio fare le barre in Canva/Figma con i valori veri, e usare il generatore solo per lo stile.

## Template J — Chat / messaggio del cliente (per S4)
```
Screenshot realistico di uno smartphone in mano, ripreso di 3/4 con luce calda da interno,
schermo con un'app di messaggistica generica (nessun logo, nessun nome di app riconoscibile).
Un solo messaggio ricevuto, grande e leggibile: "[MESSAGGIO DEL CLIENTE, max 10 parole, es. 'Ci risentiamo dopo le ferie, grazie!']",
con l'orario "[ORA, es. 23:47]" e la spunta di lettura. Sotto, la tastiera aperta e nessuna risposta scritta.
Sfondo sfocato: interno di un'auto o una scrivania. Angolo in basso a destra libero per il logo (nessun logo generato). Formato 4:5.
```

## Template K — Scritto a mano (per S1, S3)
```
Fotografia realistica di [una lavagna bianca in una piccola sala riunioni / un foglio a quadretti su una scrivania / un post-it su un monitor],
ripresa di 3/4 con luce naturale. Scritto a pennarello nero, grafia vera e un po' storta: "[TESTO, max 8 parole o 4 righe brevi]".
[ELEMENTO DI TENSIONE, es. "il numero 1,5 cerchiato tre volte in rosso, con una freccia"]. Qualche segno di cancellatura vecchia sullo sfondo.
Niente persone. Angolo in basso a destra libero per il logo (nessun logo generato). Formato 4:5, 1080x1350.
```
Meglio ancora: scriverlo davvero e fare la foto col telefono (2 minuti, e la grafia è vera).

## Template L — Foto vera dell'autore (per S3, S5) — da scattare, non da generare
```
FOTO DA FARE:
- L'autore in un posto vero del suo lavoro (auto, sala riunioni, scrivania con il portatile aperto), luce naturale.
- Un oggetto che porta l'idea del post in mano o vicino (il foglio con i punteggi, il telefono, il preventivo).
- Espressione vera (pensierosa, ironica), non la posa da profilo. Verticale 4:5, scattata col telefono va benissimo.
- Facoltativo: una parola o un numero in ambra #F9A517 sovrapposto in Canva, max 3 parole.
```
