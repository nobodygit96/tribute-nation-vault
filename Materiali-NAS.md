---
tags: [kb, nas, materiali, storage, MARKETING]
aggiornato: 2026-08-17
---

# Materiali NAS — Indice e Regole di Salvataggio

← [[_CLAUDE-TRIBUTE-NATION|Indice]]

## Accesso

Il NAS è raggiungibile come cartella di rete già mappata su Windows: **`Z:\`** → `\\NASNEW\Documenti`. Claude ci accede direttamente come a qualunque cartella locale (nessuna configurazione aggiuntiva). Il perimetro di lavoro è **`Z:\TRIBUTE NATION\`** — le altre cartelle di primo livello sul NAS (CASA, VALERIA, DANIELE, FIRME, CREDENZIALI) sono personali/fuori perimetro, non toccarle.

## Mappa cartelle (primo livello dentro `TRIBUTE NATION\`)

| Cartella | Contenuto |
|---|---|
| `Band della nation\<NomeBanda>\` | Materiale grezzo (foto, loghi) + pacchetto spotlight finito per ogni band — una sottocartella per band, ~55 attualmente |
| `GRAFICHE POST\` | Grafiche finite pronte per pubblicazione (bside, spoiler, ads, entra nella nation, ecc.), perlopiù flat |
| `CALENDARIO_STORIE\` | Render settimanali (lunedì…domenica) per la story "Programmazione settimanale" |
| `DALLA NATION PER LA NATION\<data>\` | Pacchetti datati per il contenuto del venerdì |
| `FOTOGRAFI\<Nome fotografo>\` | Materiali/articoli per fotografi collaboratori (es. Gianmarco Bumbaca / Luce Rossa) |
| `VIDEO\<banda>\` | Video per band (finora solo Flammen) |
| `VenueDaPubblicare\<Locale>\` | Foto locale, in coda — stesso pattern "in coda" del Venue Tracker Notion |
| `VenuePubblicati\<Locale>\` | Foto locale, dopo pubblicazione — spostare qui da sopra a lavoro finito |
| `LogMonitor\tn-monitor-sicurezza.csv` | Log del Monitor interno di Daniele (vedi [[Funzionalita-Sito-e-Area-Riservata]]) |
| `POST CALENDARIO\<DD_DD_MESE_ANno>.zip` | Carosello "Live della Nation" (contenuto del lunedì, vedi [[Calendario-Editoriale]]): roundup settimanale di tutti i live delle band della Nation, uno zip a settimana con slide numerate (cover + una per giorno con live programmati + chiusura "alla prossima settimana") |
| `TributeNation\` | Cartella mista: loghi brand (`LOGO_*.png/.psd`), asset sito, briefing/questionario, bundle deploy PHP (`SitoPhP\`), story "Live della settimana" (`calendario\`). Contiene anche `OBSIDIAN_TN\` — **uno snapshot vecchio e disallineato della KB** (ha ancora `Benvenuto.md`, eliminato dalla KB vera il 2026-08-16): non è una fonte di verità, ignorarlo. |

## Pattern dentro ogni cartella band (`Band della nation\<Nome>\`)

**Allineamento eseguito il 2026-08-16**: i nomi delle 56 cartelle band sono stati confrontati uno per uno col Band Tracker Notion (verifica diretta pagina per pagina, non solo ricerca semantica — alcuni match automatici erano falsi positivi, es. "SEXTAPE" sembrava "Sex Sells"/Bon Jovi ma il press kit nella cartella conferma che è una tribute band Deftones senza pagina Notion propria). 28 cartelle rinominate per matchare esattamente il campo "Nome Band" su Notion (es. `FromZero` → `Frøm Zerø`, `HABANERO` → `Habanero`, `TheParalyzed` → `The Paralyzed`). Ogni cartella band ha ora una sottocartella **`Spotlight\`** (standardizzata da `files\`/`materiali\`/case diverse dove già esisteva un pacchetto, creata vuota dove non esisteva ancora nulla) — segue la regola 3 del [README sul NAS](#regole-generali-per-salvare-nuovo-materiale-proposta-da-confermare-con-vale).

- **Materiale grezzo** ricevuto dalla band (foto, logo) sta sempre in root della cartella.
- Il **pacchetto finito** (9 slide 1080×1080 + caption PDF + articolo PDF/HTML) va nella sottocartella `Spotlight\`.
- Quasi ogni cartella compare ancora **doppia** (cartella estratta + `.zip` dello stesso contenuto, es. `files\` e `files.zip`) — non toccato in questo giro, resta da pulire (regola 4 del README).
- **4 cartelle NON standardizzate, lasciate come sono** perché hanno già più sottocartelle specializzate (foto/carosello/articolo separati) e un merge automatico rischiava di mescolare contenuti: **Disasterpiece** (`articolo_caption\`, `carosello\`, `files\`, `foto\`), **Supersonic Show** (`materiali\`, `PAGINA SITO\`, `Supersonic_Pacchetto\`), **Flammen** (`MATERIALI BASE SPOTLIGHT\`, con struttura annidata poco chiara), **Outshined** (`Outshined_Pacchetto\`, con una sottocartella duplicata annidata) — da riordinare a mano se si vuole uniformarle del tutto.
- **Aggiornamento 2026-08-16**: delle cartelle senza corrispettivo, **15 sono state aggiunte al Band Tracker Notion** (Stato 🔍 Da contattare), con Artista Tributato confermato controllando loghi/press kit/questionari già in cartella dove possibile: 21 Guns (Green Day), AbbaTime (ABBA), Black Sabbath Legacy (Black Sabbath), Electric Blue (non confermato), La Fattoria dei Mendicanti (Jethro Tull), Fear of the Beast (Iron Maiden), Gli Spari Sopra (non confermato), The Green River Band (Creedence Clearwater Revival), Loud and Clear (The Cranberries), Maiden Machine (Iron Maiden), Nevrotico Alcolico (Negrita), NoNoNo (non confermato), PinkAkustik (Pink Floyd — nome corretto con la K, non "PinkAcustik"), Sextape (Deftones), The Believers (non confermato). Le 10 cartelle NAS coinvolte sono state rinominate di conseguenza (`Abba Time`→`AbbaTime`, `Fattoria dei mendicanti`→`La Fattoria dei Mendicanti`, `GreenRiverBand`→`The Green River Band`, `Loud&Clear`→`Loud and Clear`, `MaidenMachine`→`Maiden Machine`, `Nonono`→`NoNoNo`, `PinkAcustik`→`PinkAkustik`, `SEXTAPE`→`Sextape`, `21Guns`→`21 Guns`, `Fear of the beast`→`Fear of the Beast`) — tutte le 56 cartelle band ora combaciano col loro corrispettivo Notion (dove esiste).
- ⚠️ **"sickness" e "lost_in_south" non sono band**: sono due font scaricati (rispettivamente uno stile Slipknot chiamato "Sickness" e uno chiamato "Lost in South", entrambi con licenza "solo uso personale" di Gassstype/altri) finiti per sbaglio dentro `Band della nation\`. Non aggiunte a Notion. Vale ha scelto di lasciarle dove sono per ora (2026-08-16).
- ⚠️ **Wonderwall**: su Notion Band Tracker il nome è "Wonderwall" senza "The" — la cartella NAS è stata rinominata di conseguenza, ma KB e Notion Piano Editoriale usano ancora "The Wonderwall" (bacino sito). Da riconciliare se si vuole zero discrepanze anche lì.
- Corretto anche un refuso nel Band Tracker stesso: la pagina "HabaneroRHCP" è stata rinominata "Habanero" (nome+artista erano concatenati per errore) — coerente con cartella NAS, roster KB e sito.

## Cosa è già pronto per gli Spotlight programmati (19/08–21/10, vedi [[Calendario-Editoriale]])

Utile prima di iniziare il lavoro su uno spotlight: controllare se il pacchetto esiste già.

| Data | Band | Pacchetto spotlight sul NAS |
|---|---|---|
| 19/08 | Desaparecidos | ✅ già in `Spotlight\` |
| 26/08 | Beernow | ❌ solo materiale grezzo (2 foto + logo) |
| 26/08 | The Wonderwall | ✅ pacchetto completo in `Spotlight\` (`Wonderwall_Pacchetto.zip`, verificato 2026-08-16) — ⚠️ lo stesso zip è duplicato anche in root della cartella band, non solo in `Spotlight\`: da ripulire (vedi regola 4) |
| 02/09 | Frøm Zerø | ✅ pacchetto completo in `Spotlight\` (`FromZero_Pacchetto.zip` + file singoli: Articolo/Caption in md, WordPress HTML, PDF branded, logo, 9 slide), prodotto e verificato il 2026-08-16 — l'email di intake originale (`SpotlightFromZero.pdf`) resta nella stessa cartella come riferimento, non è stata cancellata |
| 09/09 | Wild Berries | ✅ già in `Spotlight\` |
| 16/09 | Jar | ✅ già in `Spotlight\` |
| 23/09 | The Paralyzed | ✅ già in `Spotlight\` |
| 30/09 | Living Park | ✅ già in `Spotlight\` |
| 07/10 | Black Sabbath Legacy | ✅ già in `Spotlight\` |
| 14/10 | 21 Guns | ✅ già in `Spotlight\` |
| 21/10 | Napoli Blues | ✅ già in `Spotlight\` (cartella rinominata da `Napolin blues\` il 2026-08-16) |

Solo Beernow (26/08, lo slot doppio con The Wonderwall ancora da risolvere con Vale) parte da zero — The Wonderwall e Frøm Zerø hanno entrambi il pacchetto pronto (vedi sopra). Nota: Frøm Zerø è materiale di prova generato da Claude per validare gli standard di produzione, non ancora passato per revisione editoriale completa prima della pubblicazione.

🔧 **Attendibilità dei ✅ in questa tabella da riverificare**: il ✅ di Frøm Zerø si basava solo sulla presenza di un file dentro `Spotlight\`, non sul suo contenuto reale — era in realtà solo materiale grezzo (email di intake). Le altre righe ✅ (Wild Berries, Jar, The Paralyzed, Living Park, Black Sabbath Legacy, 21 Guns, Napoli Blues) sono state marcate con lo stesso criterio superficiale e non ancora riaperte una per una: possibile che alcune abbiano lo stesso problema.

## Regole generali per salvare nuovo materiale (proposta, da confermare con Vale)

1. **Una cartella per band** in `Band della nation\`, nome identico a quello usato in Notion Band Tracker (stessa capitalizzazione) — evita refusi tipo "Napolin blues".
2. **Materiale grezzo appena arriva** (foto, loghi, saluto della band) va subito in root della cartella band — non aspettare di avere tutto il set per crearla.
3. **Pacchetto spotlight finito** sempre in una sottocartella chiamata `Spotlight\` (non più `files`/`materiali`/nomi custom) — nome prevedibile, cercabile da chiunque (incluso Claude).
4. **Non tenere sia lo zip che la cartella estratta** per lo stesso contenuto — solo la cartella estratta; lo zip va cancellato dopo l'estrazione.
5. **Venue**: stesso pattern già in uso — `VenueDaPubblicare\<Locale>\` finché non pubblicato, poi spostare in `VenuePubblicati\<Locale>\` (coerente col Venue Tracker Notion).
6. **Nomi file dentro `Spotlight\`**: seguire lo schema già usato da Desaparecidos/RATS — `<banda>_slideN_tema.png`, `<banda>_caption.pdf`, `<banda>_articolo.pdf` — rende il set riconoscibile a colpo d'occhio.

## Vedi anche

- [[Strumenti-e-Risorse]]
- [[Pipeline-Contenuti-e-Roster]]
- [[Produzione-Grafica-Social]]
- [[Calendario-Editoriale]]
