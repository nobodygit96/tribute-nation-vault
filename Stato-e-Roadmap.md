---
tags: [kb, stato, roadmap, todo, MARKETING, WEB]
aggiornato: 2026-08-16
---

# Stato Attuale e Roadmap

← [[_CLAUDE-TRIBUTE-NATION|Indice]]

## In corso / completato

> Verifica diretta su tributenation.it e riassunto da Daniele (vedi [[Funzionalita-Sito-e-Area-Riservata]], [[Strategia-Mercato-e-Sviluppo]], [[LOG]]).

- **13 spotlight pubblicati e confermati live** sul blog del sito: Eponymous, RATS, Disasterpiece, KoRnea, Again, KissMyStarfish, Habanero, Outshined, Paradise Roses, Supersonic Show, Flammen, Mr. Crowley, 2nd Sucks (+ Luce Rossa, dal briefing precedente, non ritrovata singolarmente sul sito).
- **47 band con pagina pubblicata** su tributenation.it/area-band/ (contro le 80+ tracciate nel Band Tracker Notion), di cui 34 senza ancora uno spotlight — bacino diretto per i prossimi (dettaglio in [[Pipeline-Contenuti-e-Roster]]).
- **73 eventi/date live** in calendario sul sito (fonte: Daniele, 2026-08-16, non riverificato via conteggio diretto).
- **Bot Telegram pubblico dal 21/07/2026**, copertura 107 città italiane.
- **Login self-service per le band** in produzione dal 03-04/08/2026: registrazione, rivendicazione band, modifica autonoma scheda (dettagli in [[Funzionalita-Sito-e-Area-Riservata]]).
- **Filtri di ricerca band** (nome, artista tributato, genere) attivi dall'8/08/2026 — verificati presenti su `/area-band/`.
- **Il Monitor**: cruscotto interno di sola lettura per Daniele/Nobody (versione v6 dell'11/08/2026), non un servizio clienti — dettagli in [[Funzionalita-Sito-e-Area-Riservata]].
- Hub "Entra nella Nation" con i 3 form (Pagina sito, Spotlight, Calendario date) verificato live e funzionante come da [[Stack-Tecnico-Sito]].
- Calendario editoriale pianificato 13 giugno – 12 luglio 2026, inserito in Notion.
- Nuove note [[Produzione-Grafica-Social]], [[Funzionalita-Sito-e-Area-Riservata]], [[Strategia-Mercato-e-Sviluppo]].

## On the horizon

- Completare i template story Canva mancanti con coerenza visiva (vedi [[Pipeline-Contenuti-e-Roster]]).
- Lancio canale WhatsApp (Telegram già lanciato — vedi sopra).
- Scouting venue e outreach in espansione continua — outreach Notion ancora fermo a "🔍 Da contattare" al 2026-06-20 (vedi [[Venue-Tracker]]); l'Area Venue pubblica sul sito è **online**, con 1 locale visibile su 6 censiti/pronti (vedi [[Venue-Tracker]]).
- Spingere le 34 band con pagina sito ma senza spotlight verso il processo Spotlight (vedi [[Pipeline-Contenuti-e-Roster]]).
- Riallineare lo Stato su Notion (Band Tracker/Piano Editoriale) con lo stato reale sul sito — **da tentare ogni sera da Claude** (2026-09-03), entry per entry via `notion-search`/`notion-fetch` (query bulk non disponibili, vedi [[Strumenti-e-Risorse]]); se impraticabile, promemoria esplicito a Vale invece di lasciarlo scivolare.
- Analytics sito (GA4) non ancora attivo: nessun dato di traffico da mostrare alle band come prova di valore — gap strategico aperto, vedi [[Strategia-Mercato-e-Sviluppo]].
- ~~Campo email/referente sulla scheda band: manca~~ — **corretto 2026-09-03, esisteva già**: campo pubblico "Email di contatto" sulla scheda band dal 07/08/2026 (obbligatorio nei form, offuscato anti-scraping) e colonne "Nome Gestore"/"Email Gestore" nel Monitor interno per ogni band che ha rivendicato la pagina (fonte: KB tecnica di Daniele, `reference/scheda-band.md` Round 10). Copre però solo le band che hanno **già rivendicato** la pagina, non tutte le 47 con pagina pubblica né le 80+ del Band Tracker. Da chiarire: quante l'hanno fatto, e se quel dato è già esportabile verso Brevo per l'outreach o va ancora collegato.
- Idee di sviluppo prodotto (EPK scaricabile, date portabili, "segui la band" su Telegram, matching band↔locale, pacchetto a pagamento per i locali): nessuna decisa, solo proposte — vedi [[Strategia-Mercato-e-Sviluppo]].
- 🔧 **Da capire (aggiunto da Vale, 2026-09-04)**: sul fronte cybersecurity e assicurazioni, se e come TN debba procedere per il sito (polizza, requisiti minimi di sicurezza); e se ci sono obblighi da rispettare per l'AI Act (Regolamento UE 2024/1689, in vigore dal 2 agosto 2026) rispetto a come TN usa già l'AI nei contenuti. Nessuna ricerca fatta ancora, solo segnalato.

### Cosa NON è ancora vero (da non comunicare come attivo)

Analytics GA4, campo email pubblico sulla scheda band, Area Fan con account, il Monitor come funzionalità clienti — lista completa e dettagliata in [[Funzionalita-Sito-e-Area-Riservata]]. (L'Area Venue è invece confermata online — vedi riga sopra e [[Venue-Tracker]].)

## Correzioni pendenti

1. ~~Articolo Flammen (CMS WordPress): rimuovere "tribute Rammstein tedeschi" dopo "i GGG"~~ — **risolto** (vedi [[Pipeline-Contenuti-e-Roster]]).
2. ~~Handle Instagram Mr. Crowley~~ — **risolto** (vedi [[Pipeline-Contenuti-e-Roster]]).
3. Handle @sleepwalkersitalia (2nd Sucks): l'articolo live nomina "Sleepwalkers" ma senza handle @ nel testo — 🔧 verificare se il controllo riguardava solo la caption IG (non ricontrollata in questa sessione) e non l'articolo del sito.

## Metriche Meta (luglio 2026)

> Snapshot dal briefing 2026-08-16, non ricontrollato su Meta in questa sessione.

- Follower Facebook: 154 · Instagram: 400
- Copertura settimanale: FB ~6.211 · IG ~3.666
- Visualizzazioni (28gg): 37.038
- Interazioni contenuti: 133 (+160,8%)
- Visite FB: 1.064 (+383,6%)
- Follower netti: 96 (+81,1%)

## Bug aperti sul sito 🔧 DA COMPLETARE

Nessuno documentato finora (a parte le correzioni pendenti sopra, che sono correzioni di contenuto/copy, non bug tecnici).

## Vedi anche

- [[Pipeline-Contenuti-e-Roster]]
- [[Produzione-Grafica-Social]]
- [[Funzionalita-Sito-e-Area-Riservata]]
- [[Strategia-Mercato-e-Sviluppo]]
- [[Stack-Tecnico-Sito]]
- [[LOG]]
