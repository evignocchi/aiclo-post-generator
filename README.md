# aiclo-post-generator

Guide in Markdown per generare post LinkedIn che fanno like e commenti per **Aiclo**, scritti per **manager commerciali e venditori** delle PMI italiane.

## Come si usa
Apri la repo con Claude (o con un altro assistente AI) e chiedi, per esempio:

> "Scrivimi un post per Simone sui venditori che non fanno follow-up."

> "Dammi 3 post per Andrea, uno per manager e due per venditori, strutture diverse."

L'assistente segue `CLAUDE.md`, che gli dice cosa leggere, come scrivere e in che formato restituire **il testo e, se serve, il prompt per generare la grafica**.

## Struttura
| File | Contenuto |
|------|-----------|
| `CLAUDE.md` | Le istruzioni operative per il generatore |
| `HANDOFF-GROK.md` | Le istruzioni aggiuntive per l'agente Grok: GitHub, immagini con ChatGPT e logo, connettore Aiclo |
| `guide/01-analisi-post-benchmark.md` | I 18 post di riferimento: categorie, peculiarità, engagement |
| `guide/02-anatomia-post-vincente.md` | Sintesi incrociata: le 11 leggi, le 7 strutture, il mix editoriale |
| `guide/03-icp-aiclo.md` | Il prodotto, i claim, l'ICP, le due persone |
| `guide/04a-manager.md` | Mappa dell'empatia del manager: cosa pensa, vede, sente, dice e fa; paure con origine e trigger |
| `guide/04b-venditore.md` | Mappa dell'empatia del venditore, con i 4 tipi di venditore |
| `guide/04c-scontro-e-terreno-comune.md` | La stessa funzione letta da manager e venditore, i temi comuni, il vincolo dei social |
| `guide/05-tono-di-voce.md` | Il tono, il lessico, le parole vietate, la formattazione |
| `guide/06-hook-e-chiusure.md` | La libreria di aperture e chiusure |
| `guide/07-prompt-grafiche.md` | Quando usare una grafica e i template dei prompt |
| `guide/08-checklist-qualita.md` | La checklist prima di pubblicare |
| `guide/09-banca-spunti.md` | Aperture pronte per manager, venditori ed entrambi, e il contesto italiano |
| `ricerca/` | Il profilo psicologico del target con le fonti, e i risultati dei test |
| `brand/` | Logo (nero e bianco) da sovrapporre alle grafiche |
| `dati/` | Insight aggregati (l'unica fonte di statistiche oltre ai claim del sito), episodi e clienti da usare come spunto |
| `post/` | Una cartella per autore (`andrea-aureli/`, `damiano-aureli/`, `simone-continenza/`), con il `profilo.md` e i post generati. `_template-autore/` serve per aggiungerne altri |
| `esempi/` | Post d'esempio già completi |
| `domande-aperte.md` | Le decisioni prese e quello che manca |

Obiettivo dei post: **solo engagement**. Aiclo si nomina raramente.
