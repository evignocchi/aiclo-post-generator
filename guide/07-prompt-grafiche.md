# 07 — Grafiche: quando servono e i prompt per generarle

## Quando mettere una grafica
Dai post di riferimento: i vincenti sono **testo semplice** oppure hanno **un video nativo** (#16, #4) o **un'immagine metafora** (#17, #9). Le infografiche-lista non compaiono fra i vincenti.

| Struttura del post | Visual consigliato |
|--------------------|--------------------|
| S1 Ribaltamento | Nessuno, oppure una card tipografica con la frase finale |
| S2 Concetto con nome | **Immagine metafora** (oggetto assurdo o simbolico) |
| S3 Confessione manager | Nessuno, oppure una foto reale dell'autore |
| S4 Dentro la trattativa | **Card "trascrizione"** (la battuta del cliente in stile chat) oppure uno screenshot (anonimizzato) dello scorecard Aiclo |
| S5 Storia dal campo | Foto reale (mai generata con l'AI) |
| S6 Formula / strumento | **Infografica / carosello PDF** (qui sì) |
| Meme | Immagine meme |

## Brand (da confermare: vedi `domande-aperte.md`)
```
BRAND_PRIMARY   = [HEX da fornire]
BRAND_ACCENT    = [HEX da fornire]
BRAND_DARK      = #0F172A (provvisorio)
BRAND_LIGHT     = #F8FAFC (provvisorio)
FONT            = sans-serif geometrico, tipo Inter / Manrope (provvisorio)
LOGO            = wordmark "Aiclo", piccolo, in basso a destra
FORMATO         = 1080x1350 (4:5) per il feed; 1080x1080 per i caroselli
```

## Regole valide per ogni prompt
- Una sola idea visiva per immagine.
- Massimo 12 parole di testo nell'immagine (i generatori sbagliano le scritte: verificare sempre).
- Niente stock photo di strette di mano, grafici che salgono o robot.
- Persone realistiche, contesto italiano (auto aziendale, capannone, cucina di un cliente, ufficio di una PMI), mai Silicon Valley.
- Nessun volto riconoscibile di persone reali, nessun logo di terzi.

---

## Template A — Immagine metafora (per S2)
```
Fotografia editoriale concettuale, luce naturale morbida, composizione minimalista,
sfondo neutro chiaro (#F8FAFC). Soggetto: [OGGETTO ASSURDO CHE RAPPRESENTA IL CONCETTO,
es. "un binocolo con il 95% delle lenti coperto da nastro adesivo nero"].
Stile: realistico, still life, alto contrasto, profondità di campo ridotta.
Nessun testo nell'immagine. Formato 4:5, 1080x1350.
```

## Template B — Card "trascrizione" (per S4)
```
Grafica flat, sfondo [BRAND_DARK]. Al centro una bolla di chat stile trascrizione,
etichetta piccola in alto "Cliente · min 23:14", testo grande in bianco:
"[BATTUTA DEL CLIENTE, max 10 parole]".
Sotto, una seconda bolla più piccola e opaca, etichetta "Venditore", testo:
"[RISPOSTA DEL VENDITORE, max 8 parole]".
In basso a destra il wordmark "Aiclo" piccolo. Font sans-serif geometrico, molto spazio vuoto.
Formato 4:5, 1080x1350.
```

## Template C — Card tipografica (per S1 / la chiusura)
```
Poster tipografico minimalista, sfondo [BRAND_LIGHT], una sola frase centrata in nero,
font sans-serif bold molto grande: "[FRASE, max 10 parole]".
Una parola evidenziata con [BRAND_ACCENT]. Nessun altro elemento tranne il wordmark
"Aiclo" piccolo in basso. Formato 4:5.
```

## Template D — Infografica / slide di carosello (per S6)
```
Slide di carosello LinkedIn, formato 1080x1080, stile editoriale pulito,
sfondo [BRAND_LIGHT], titolo in alto bold: "[TITOLO, max 6 parole]".
Contenuto: [N] blocchi numerati in verticale, ognuno con un numero grande in [BRAND_ACCENT]
e una riga di testo nero: 1) "[...]" 2) "[...]" 3) "[...]".
Icone lineari sottili, nessuna foto. Footer: "Aiclo · [n]/[totale]". Molto spazio bianco.
```
Per i caroselli: generare una slide alla volta con lo stesso prompt base e cambiare solo il contenuto. Copertina = hook del post.

## Template E — Meme (per i post meme)
```
Fotografia realistica, stile candid un po' sgranato, [SCENA IRONICA, es. "agente di commercio
italiano di 45 anni in giacca, seduto in una Fiat Panda in un parcheggio industriale al tramonto,
mangia un panino, con un preventivo cartaceo appoggiato sul volante"]. Espressione stanca ma
ironica. Nessun testo nell'immagine (il setup va nel testo del post). Formato 4:5.
```

## Template F — Mockup della dashboard (solo per i rari post sul prodotto)
Meglio **uno screenshot reale** di Aiclo con dati demo (i nomi fittizi del sito vanno bene). Se serve generarlo:
```
Mockup di un laptop su una scrivania di legno, schermo con una dashboard SaaS pulita:
matrice 2x2 etichettata "Star / In crescita / Da supportare / A rischio" con dei puntini colorati,
a fianco una heatmap. Interfaccia in italiano, colori [BRAND_PRIMARY]. Luce naturale, prospettiva 3/4.
```
