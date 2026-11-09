# 07 — Grafiche: quando servono e i prompt per generarle

## Quando mettere una grafica
Dai post di riferimento: i vincenti sono **testo semplice** oppure hanno **un video nativo** (#16, #4) o **un'immagine metafora** (#17, #9). Le infografiche-lista non compaiono fra i vincenti.

| Struttura del post | Visual consigliato |
|--------------------|--------------------|
| S1 Ribaltamento | Nessuno, oppure una card tipografica con la frase finale |
| S2 Concetto con nome | **Immagine metafora** (oggetto assurdo o simbolico) |
| S3 Confessione manager | Nessuno, oppure una foto reale dell'autore |
| S4 Dentro la trattativa | **Card "trascrizione"** (la battuta del cliente in stile chat) oppure uno **screenshot reale** della scorecard Aiclo con dati demo (Template F) |
| S5 Storia dal campo | Foto reale (mai generata con l'AI) |
| S6 Formula / strumento | **Infografica / carosello PDF** (qui sì) |
| Meme | Immagine meme |

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
FORMATO         = 1080x1350 (4:5) per il feed; 1080x1080 per i caroselli
```

### Logo nelle grafiche
I generatori di immagini **sbagliano i loghi**. Regola: nel prompt chiedere sempre **"lascia libero l'angolo in basso a destra, nessun logo"** e poi **sovrapporre il PNG vero** (`brand/logo-bianco.png` o `brand/logo-nero.png`) in Canva/Figma, largo circa il 15% della grafica, con un margine di 48px.
Nei template qui sotto è già scritto così: "spazio vuoto per il logo (nessun logo generato)".

Regola: **sfondo scuro + bianco + un tocco di ambra**. Le card chiare si usano solo come eccezione (per esempio una citazione su sfondo `#FEF7E0`).

## Regole valide per ogni prompt
- Una sola idea visiva per immagine.
- Massimo 12 parole di testo nell'immagine (i generatori sbagliano le scritte: verificare sempre).
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
Slide di carosello LinkedIn, formato 1080x1080, stile editoriale pulito,
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
- Ritaglio sul dettaglio che serve al post, 4:5 o 1:1
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
