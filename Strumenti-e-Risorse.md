---
tags: [kb, strumenti, tools, MARKETING, WEB]
aggiornato: 2026-08-16
---

# Strumenti e Risorse

← [[_CLAUDE-TRIBUTE-NATION|Indice]]

## CMS

WordPress + Elementor + tema Astra + Yoast SEO, hosting Aruba. (dettagli tecnici approfonditi in [[Stack-Tecnico-Sito]])

## Design

- **Canva:** feed post = `instagram_post`, story = `your_story`; limite di generazione per sessione, reset ~1 ora.
- **Slide PNG e PDF branded:** generate via Python/Pillow/reportlab con script riutilizzabili e parametrizzati in `tools/spotlight/` **dentro questo vault** (`make_slides.py`, `make_pdfs.py`, `fonts/`) — non nella cartella temp di sessione, sopravvivono tra una sessione e l'altra. Usati dalla skill `/spotlight` (vedi `.claude/skills/spotlight/SKILL.md`). Su questa macchina (Windows locale di Vale), Python 3.12 + Pillow + numpy + reportlab **non erano preinstallati**: installati il 2026-08-16/17 via `winget install Python.Python.3.12` + `pip install Pillow numpy reportlab` — verificare che siano ancora presenti a inizio sessione prima di assumerli disponibili (`python -c "import PIL, numpy, reportlab"`). Font Bebas Neue e DM Sans scaricabili da `raw.githubusercontent.com/google/fonts/main/ofl/...` (attenzione: `github.com/.../raw/...` per DM Sans restituisce una pagina HTML, non il font — usare sempre il dominio `raw.githubusercontent.com`). Logo TN per il footer slide/PDF: `tools/spotlight/assets/LOGO_ORIZZONTALE_RED.png`, **versionato nel repo** (non più referenziato dal NAS) — così gli script funzionano identici su qualunque macchina senza bisogno di `Z:\` mappato. Copiato dal NAS il 2026-08-17, fonte originale resta `Z:\TRIBUTE NATION\TributeNation\LOGO_ORIZZONTALE_RED.png` se serve rigenerare/aggiornare l'asset.

## Email marketing

Brevo — gestione consenso, privacy policy.

## Notion MCP

- `notion-create-pages` con `parent` come `data_source_id`
- `notion-create-view` per viste calendario/board
- Le chiamate ALTER COLUMN vanno divise per set di opzioni grandi
- L'eliminazione pagine non è supportata via MCP (rinominare per eliminazione manuale)
- Il "favoriting" va fatto manualmente
- **Limite piano (verificato 2026-06-20):** `notion-query-data-sources` (SQL) e `notion-query-database-view` (per vista) richiedono entrambi un piano Business/Enterprise con Notion AI — **non disponibili** sul piano attuale. Per leggere righe reali, l'unica via è `notion-search` (full-text, restituisce snippet) + `notion-fetch` pagina per pagina (restituisce le proprietà complete di quella riga). Niente lettura bulk: pianificare le sessioni di verifica dati di conseguenza.
- Database Piano Editoriale (calendario): [apri](https://app.notion.com/p/21da1e23a65e4001a794115733c4c46a) — ID `21da1e23a65e4001a794115733c4c46a`, data source `58f1ec40-2acc-44d6-b13f-b6738978dc5b`
- Database Band Tracker: [apri](https://app.notion.com/p/c9434a8709514990939250731ad5902d) — ID `c9434a87-0951-4990-9392-50731ad5902d`, data source `8864ed79-122f-4dd2-bc5a-91d2f14972f9` (vedi [[Pipeline-Contenuti-e-Roster]])
- Database Venue Tracker: [apri](https://app.notion.com/p/ac99a87be49a44f59a8d14639f455031) — ID `ac99a87b-e49a-44f5-9a8d-14639f455031`, data source `811bdb1d-e567-4d1b-a111-ae5aca6d07fe` (vedi [[Venue-Tracker]])

## Storage nei widget chat

- `window.storage.get/set` con chiave `tn-editorial-calendar`
- I file HTML standalone usano `localStorage`

## Google Drive — Approvazioni Spotlight (band)

- **Account da usare sempre**: `nobody.tribute.nation@gmail.com` (persona "Nobody", vedi [[Identita-e-Ruolo]]) — mai l'account personale di Vale (`valeria.0960@gmail.com`), anche se è quello che si apre di default nel browser/nell'app Drive su questo PC. Verificare l'account attivo prima di condividere qualunque cosa.
- **Cartella madre condivisa**: `Approvazioni Spotlight`, dentro "Il mio Drive" dell'account nobody. Link pubblico (chiunque abbia il link, Visualizzatore): https://drive.google.com/drive/folders/1Hv2TevgqdKaEFfNIQulaMWUOLfHWUnnF — le sottocartelle create dentro ereditano automaticamente lo stesso permesso, non serve condividerle una per una. Una sottocartella per band.
- **Su questo PC** (Vale), Google Drive Desktop è installato e sincronizza su `G:\Il mio Drive\` — creare/copiare file lì (via Bash/PowerShell) è il modo più veloce, sync automatico.
- 🔧 **Percorso tecnico per la condivisione (link/permessi)**: **non è possibile farlo da Esplora File** — sia l'app nativa "Esplora file" sia l'app "Google Drive" (che su Windows è solo un driver, apre comunque Esplora File) sono concesse a tier "click": niente tasto destro, il pannello di condivisione nativo di Windows non è visibile/controllabile. L'unica via che funziona è il **browser (estensione Claude in Chrome)**: aprire drive.google.com, verificare/cambiare account dall'icona profilo in alto a destra (i vari account Google sono già autenticati nel browser, basta selezionarli, non serve login), poi tasto destro sulla cartella → Condividi → Condividi → Accesso generale → "Chiunque abbia il link" → Visualizzatore → Copia link (poi leggibile da clipboard via `Get-Clipboard` in PowerShell). Il browser via `computer-use` nativo NON funziona per questo (i browser sono sempre concessi in sola lettura lì).

## Questo vault è ora un repository git (dal 2026-08-17)

- **Repo**: [`nobodygit96/tribute-nation-vault`](https://github.com/nobodygit96/tribute-nation-vault) (privato). Identità git locale: `Nobody_Git96` / email noreply di `nobodygit96` — stessa identità condivisa usata su `tribute-nation-kb`.
- **Perché**: la skill `spotlight` referenziava 6 note + 2 script che vivevano solo qui, mai su git — rotta per chiunque non avesse questo vault in locale (Daniele l'ha scoperto via audit). Dettagli completi in `sessioni/2026-08-17_root-cause-analysis-spotlight-skill.md` dentro `tribute-nation-kb`.
- **`.claude/skills/spotlight/`**: ora file reale in questo repo (prima raggiungibile solo via junction NTFS verso `tribute-nation-kb`) — verificato con un clone pulito in una cartella temporanea: tutti i wikilink e gli script risolvono.
- **`.claude/agents/`**: resta una junction locale verso `tribute-nation-kb` (agenti `tn-deploy-reviewer`, `tn-second-opinion`, dominio sito) — **esclusa da git qui** (`.gitignore`) per non duplicarla. Su questa macchina funziona comunque per comodità; da un clone pulito del vault, quegli agenti semplicemente non ci sono (corretto: non sono di questo dominio).
- **`.gitignore`**: solo `.obsidian/` (stato locale dell'app, non contenuto).
## Sync automatico giornaliero — `tribute-nation-vault`

Task Windows `TributeNationVault-DailySync`, ogni giorno alle 22:10 (5 minuti dopo il sync di
`tribute-nation-kb`, per non farli girare in contemporanea): script
`C:\Users\vmann\Documents\tnkb-sync\vault-daily-sync.ps1` su questo vault. Stessa identica logica
del sync di `tribute-nation-kb` (commit modifiche locali → pull → push, si ferma senza forzare in
caso di conflitto). Log in `C:\Users\vmann\Documents\tnkb-sync\logs\` (prefisso `sync-vault-`).
Testato manualmente il 2026-08-17, verde — ha anche beccato e corretto un `__pycache__/` finito
per errore nel commit iniziale (aggiunto a `.gitignore`).

🔧 Stessa limitazione dell'altro sync: gira solo se il PC è acceso alle 22:10.

## NAS

Materiali (foto/loghi band, grafiche, video) su NAS montato come `Z:\` (`\\NASNEW\Documenti`), cartella di lavoro `Z:\TRIBUTE NATION\`. Mappa completa, pattern e regole di salvataggio in [[Materiali-NAS]].

## KB condivisa (GitHub) e tool `tnkb`

- Repo KB tecnica condivisa (di Daniele, separata da questo vault Obsidian): [`9bleed0-dev/tribute-nation-kb`](https://github.com/9bleed0-dev/tribute-nation-kb) (privato), clonato in `C:\Users\vmann\Documents\Tribute Nation KB`.
- CLI di consultazione (`.NET 10`): [`9bleed0-dev/TributeNationKB.Cli`](https://github.com/9bleed0-dev/TributeNationKB.Cli), clonato in `C:\Users\vmann\Documents\TributeNationKB.Cli`, build in `bin\Debug\net10.0\TributeNationKB.Cli.exe`. Legge la KB dal path in `TN_KB_PATH` (env var utente permanente, già impostata sul percorso sopra).
- Comandi verificati: `roots` (diagnostica path), `brief` (rito di apertura sessione: TODO, segnalazioni, changelog).
- In sospeso: `monitor`/`snippet` richiederanno un'Application Password WordPress in `TN_MONITOR_USER`/`TN_MONITOR_APP_PASSWORD` — non ancora configurate, non servono per l'uso base.
- Ambito: questa è la KB **tecnica/sito** di Daniele, distinta da questo vault Obsidian (**social/contenuti**, di Vale) — vedi nota in [[Identita-Visiva]].

## Skill e agenti Claude Code (collegamento vivo)

`.claude/agents/` e `.claude/skills/` (5: `tn-deploy-snippet`, `tn-fine-sessione`, `tn-health-check`, `tn-workflow-sviluppo`, `refresh-kb-cli`) sono **junction NTFS** verso le cartelle omonime in `Tribute Nation KB\.claude\` (repo di Daniele); `settings.json` è un **hard link** allo stesso file lì. Creati il 2026-08-16 — nessuno dei due richiede Modalità sviluppatore o privilegi elevati (a differenza di un vero symlink). Claude Code carica skill/agenti solo dal `.claude/` della cartella su cui è radicata la sessione: le due cartelle di lavoro sono fisicamente separate su disco, questo collegamento le fa apparire come se fossero nella stessa.

Sempre sincronizzato: un aggiornamento di Daniele nel suo repo si riflette qui **senza bisogno di ricopiare nulla**. Se in futuro `git pull` su `Tribute Nation KB` rinomina/elimina una skill, la junction segue automaticamente lo stato della cartella target.

🔧 `refresh-kb-cli` contiene comunque un percorso hardcoded della macchina di Daniele (`C:\Users\utente\...`) nel proprio testo — da correggere a mano se mai scattasse su questa macchina, il collegamento non risolve quello. Non verificato se la sessione già aperta al momento della creazione del link li riconosce a caldo — da confermare alla prossima sessione aperta da questa cartella.

## Sync automatico giornaliero — `tribute-nation-kb`

Task di Windows Task Scheduler `TributeNationKB-DailySync`, ogni giorno alle 22:00: script
`C:\Users\vmann\Documents\tnkb-sync\daily-sync.ps1` su `Tribute Nation KB` (repo condiviso con
Daniele). Ordine: **commit** delle modifiche locali non ancora salvate (se ce ne sono) → **pull** →
**push** (solo se c'è qualcosa da mandare). Se il pull trova un conflitto, **si ferma senza toccare
altro**: nessun merge forzato, nessuna sovrascrittura — il repository resta così com'è finché non lo
risolvi a mano. Log di ogni esecuzione in `C:\Users\vmann\Documents\tnkb-sync\logs\`.

🔧 Gira solo se il PC è acceso a quell'ora (Task Scheduler di Windows non riavvia/sveglia la
macchina di default). Non copre la tua vault Obsidian locale (questa cartella): non è ancora un
repository git, quindi non ha backup su GitHub — solo `tribute-nation-kb` è coperto da questo sync.

## Sync automatico settimanale — `TributeNationKB.Cli`

Task `TributeNationKBCli-WeeklySync`, ogni sabato alle 23:00: script
`C:\Users\vmann\Documents\tnkb-sync\weekly-sync-cli.ps1`. Stessa logica commit → pull → push del
sync giornaliero della KB, con un controllo in più perché è codice: prima di pushare, se ci sono
commit locali, gira `dotnet build` + `dotnet test` (la stessa suite che verifica anche la GitHub
Action). **Se build o test falliscono, non pusha**: il commit resta locale, non pushato, finché non
lo controlli a mano — niente codice rotto spinto automaticamente sul repo condiviso. Log in
`C:\Users\vmann\Documents\tnkb-sync\logs\` (prefisso `sync-cli-`).

## Vedi anche

- [[Stack-Tecnico-Sito]]
- [[Regole-Operative-Claude]]
- [[Materiali-NAS]]
