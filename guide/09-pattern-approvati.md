# 09 — Cosa impariamo dai post approvati

Questo file è la **memoria** della macchina. Si aggiorna con la skill `impara` (vedi `.claude/skills/impara/SKILL.md`) ogni volta che entrano nuovi post approvati o nuovi numeri di pubblicazione.

**Prima di scrivere un post, leggi le Lezioni qui sotto (obbligatorio).** Valgono più degli esempi generici dei file 01-07, ma **mai** più delle regole non negoziabili di `CLAUDE.md`.

## Da dove imparano le lezioni (in ordine di peso)
1. **I numeri dopo la pubblicazione** (commenti e condivisioni pesano più delle reazioni). Contano solo con almeno 5 post con i numeri.
2. **Le modifiche fatte dall'umano fra la bozza e la versione approvata** (sezione "Cosa è cambiato dalla bozza" di ogni post). È il segnale più veloce: dice cosa non ci piaceva.
3. **Le scelte fatte in revisione** (per esempio l'hook scelto fra i 3 proposti, la visual rifatta).

## Lezioni
Formato di ogni lezione: regola in una riga · prova (quali post, quanti) · confidenza (bassa: 1-2 post · media: 3-5 · alta: 6+ con i numeri).

### Scrittura
- **L'hook preferito è un'accusa rivolta a noi stessi, non un numero secco.** Fra "Abbiamo dato un voto alle nostre trattative. In una fase prendiamo 1,5 su 5." e "Il mio team è bravissimo a farsi voler bene. Ed è proprio questo il problema." è stato scelto il secondo: il numero arriva subito dopo, come prova. · prova: `post/simone-continenza/2026-11-09-implicazioni-1-5.md` · confidenza: bassa
- **I numeri veri del nostro team, ammessi come errore nostro, sono materiale forte.** Il primo post approvato è costruito su un dato reale (1,5 su 5) e lo racconta come confessione. · prova: 1 post · confidenza: bassa

### Visual
- **Scritto a mano batte la card scura.** La card tipografica su sfondo nero è stata sostituita da una lavagna con il numero cerchiato in rosso. · prova: 1 post · confidenza: bassa
- **L'anomalia deve essere visibile a colpo d'occhio:** tre valori normali e uno cerchiato. · prova: 1 post · confidenza: bassa

### Prompt immagini che hanno funzionato
- Lavagna bianca in una piccola sala riunioni, ripresa di 3/4, luce naturale laterale, grafia vera un po' storta, il numero chiave cerchiato tre volte in rosso con una freccia, un pennarello ambra sul bordo come unico tocco di brand. (Il prompt completo è nella parte automatica qui sotto.)

### Da verificare (ipotesi, non ancora regole)
- I post con dati del team commerciale di Aiclo prendono più commenti dei post con dati aggregati dei clienti?
- La foto vera dell'autore batte la visual generata?

## Numeri (parte automatica)
<!-- AUTO:INIZIO -->

_Parte generata da `scripts/analizza_pattern.py`: non modificarla a mano._

**Post approvati:** 1 · **con i numeri di pubblicazione:** 0

⚠️ Servono almeno 5 post con i numeri per parlare di pattern (ora sono 0). Fino ad allora le lezioni si basano soprattutto su cosa è stato modificato fra bozza e versione approvata.

### Medie dei post approvati
- Parole: 195 · righe: 20 · parole della prima riga: 15 · numeri nel testo: 7
- Post che nominano Aiclo: 0 su 1

### Per struttura
| Struttura | Post | Con numeri | Punteggio medio |
|---|---:|---:|---:|
| S3 Confessione (dal campo) | 1 | 0 | — |

### Per meccanismo dell'hook
| Meccanismo dell'hook | Post | Con numeri | Punteggio medio |
|---|---:|---:|---:|
| Ribaltamento | 1 | 0 | — |

### Per target
| Target | Post | Con numeri | Punteggio medio |
|---|---:|---:|---:|
| Venditore | 1 | 0 | — |

### Per tipo di visual
| Tipo di visual | Post | Con numeri | Punteggio medio |
|---|---:|---:|---:|
| scritto a mano (Template K), generata. | 1 | 0 | — |

### Per autore
| Autore | Post | Con numeri | Punteggio medio |
|---|---:|---:|---:|
| simone-continenza | 1 | 0 | — |

### Classifica (solo post con i numeri)
Ancora nessun post con i numeri. Dopo la pubblicazione: `python3 scripts/metriche.py post/... --reazioni N --commenti N ...`

### Tutte le prime righe approvate
- Il mio team è bravissimo a farsi voler bene. Ed è proprio questo il problema. _(Ribaltamento · simone-continenza)_

### Prompt delle visual approvate
**post/simone-continenza/2026-11-09-implicazioni-1-5.md** · scritto a mano (Template K), generata. · punteggio —
Anomalia: tre voti "normali" e un 1,5 cerchiato in rosso, come alla lavagna di scuola.
```
Fotografia realistica di una lavagna bianca in una piccola sala riunioni di un'azienda italiana,
ripresa di 3/4 con luce naturale da una finestra a sinistra, formato verticale 4:5, 1080x1350.
Scritto a pennarello nero, grafia vera, un po' storta, quattro righe una sotto l'altra:
"Situazione 2,7"
"Problema 2,8"
"Rapport 3,2"
"Implicazioni 1,5"
Il numero "1,5" è cerchiato tre volte con un pennarello rosso, con una freccia che lo indica.
Un pennarello color ambra #F9A517 appoggiato sul bordo della lavagna. Vecchie cancellature appena visibili sullo sfondo.
Nessuna persona, nessun altro testo. Profondità di campo ridotta sul cerchio rosso.
Lasciare libero l'angolo in basso a destra per il logo (nessun logo generato).
```


<!-- AUTO:FINE -->
