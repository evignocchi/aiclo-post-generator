# Dati

| File | Cosa contiene | Come si usa |
|------|---------------|-------------|
| `insight-trattative.md` | Numeri aggregati e anonimi dalle trattative analizzate | **Solo le righe con `Approvato: sì`.** Sono l'unica fonte di statistiche oltre ai claim del file `03`. |
| `clienti-e-risultati.md` | Casi di prima e dopo | Spunti. Si possono anche costruire casi nuovi (vedi sotto). |
| `episodi-trattative.md` | Scene di trattative, anonimizzate | Spunti. Si possono anche costruire episodi nuovi (vedi sotto). |

## Regole
- **Statistiche aggregate** ("nelle trattative che analizziamo, il X%…"): solo righe approvate di `insight-trattative.md` o claim del file `03`.
- **Storie, episodi e casi di prima e dopo**: si possono costruire. Devono essere verosimili, anonimi (nessuna azienda o persona reale con il nome) e coerenti con i clienti tipici (oggi soprattutto SaaS e B2B, file `03`). Nell'output si segnalano come `storia costruita`.
- Gli episodi veri hanno la precedenza su quelli costruiti, e restano anonimi: nessun nome, azienda o dettaglio che renda riconoscibile il cliente o il venditore, salvo autorizzazione scritta.
- Quando una riga viene usata in un post, si scrive il nome del post nella colonna "Usato in", così non si riusa troppo presto.
