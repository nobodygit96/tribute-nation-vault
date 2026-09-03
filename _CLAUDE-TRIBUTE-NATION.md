---
tags: [kb, indice, MARKETING]
aggiornato: 2026-08-16
---

# Tribute Nation — Knowledge Base (Indice)

> Questa è la **fonte di verità** del progetto, ristrutturata come wiki: un'unica nota-indice che rimanda a una nota separata per ogni aspetto del progetto (così ogni aspetto si apre come tab/nota propria in Obsidian, invece di scorrere un unico file). Struttura ispirata al pattern "LLM Wiki" (Index → Wiki → Log) di Andrej Karpathy per la memoria persistente degli agenti AI — [gist originale](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Regole di manutenzione (lint, formato log) in [[Regole-Operative-Claude]].

## Come leggere questa KB

- **Ad ogni sessione:** leggi sempre [[Regole-Operative-Claude]] e [[Tone-of-Voice]] — governano qualunque output, indipendentemente dal task.
- **Poi leggi solo le note rilevanti** per il task del momento (non serve aprire tutto ogni volta).
- Se manca un'informazione e la nota dice **🔧 DA COMPLETARE**, chiedi a Vale invece di inventare.

## Struttura della KB

| Nota | Cosa contiene |
|---|---|
| [[Identita-e-Ruolo]] | Cos'è Tribute Nation, la persona "Nobody", i due co-fondatori (Vale, Daniele) e i loro ruoli |
| [[Tone-of-Voice]] | Regole di scrittura, brand voice, struttura articoli/caption |
| [[Identita-Visiva]] | Palette, font, coerenza grafica |
| [[Produzione-Grafica-Social]] | Specifiche tecniche slide/carosello/story, script Python, struttura pacchetto spotlight |
| [[Pipeline-Contenuti-e-Roster]] | Pipeline spotlight, roster band, stato template Canva |
| [[Calendario-Editoriale]] | Struttura editoriale settimanale |
| [[Venue-Tracker]] | Database Notion venue/locali per outreach live |
| [[Funzionalita-Sito-e-Area-Riservata]] | Cosa offre il sito oggi a band/locali/fan, area riservata, Monitor interno di Daniele |
| [[Strategia-Mercato-e-Sviluppo]] | Diagnosi strategica, ricerca di mercato, idee di sviluppo prodotto (non decise) |
| [[Servizi-a-Pagamento-Band]] | 🔧 Struttura decisa (3 livelli + listino a parte), prezzi fissati, ma tetti/sconti/infrastruttura pagamento ancora da chiudere |
| [[Strumenti-e-Risorse]] | CMS, Canva, Notion MCP, email marketing, storage |
| [[Team-Marketing-AI-e-Meta-Ads]] | 🔧 Bozza: ricerca su team di agenti AI dedicati e gestione Meta Ads (BM/Pixel/retargeting), da verificare e decidere passo passo |
| [[Integrazione-Google-GTM-GA4-Search-Console]] | ⏸️ Roadmap e checklist pronte, non ancora iniziata: GTM, GA4, Search Console — in attesa di accessi/decisioni da Vale |
| [[Materiali-NAS]] | Mappa cartelle NAS (Z:\), pattern materiali band/venue, regole di salvataggio |
| [[Stack-Tecnico-Sito]] | WordPress, pagine, admin, CSS, calendario eventi (per lo più 🔧 da completare) |
| [[Regole-Operative-Claude]] | Golden rules, note tecniche slide, errori noti da non ripetere |
| [[Stato-e-Roadmap]] | Stato attuale, prossimi passi, bug aperti |
| [[LOG]] | Cronologia degli aggiornamenti a questa KB |

## Skill disponibili (`.claude/skills/`)

| Skill | Cosa fa |
|---|---|
| `spotlight` | Pacchetto spotlight completo per una band (articolo, caption, HTML, 9 slide, PDF); include anche la verifica di completezza di un pacchetto già esistente |
| `statement-card` | Grafica Spoiler/B-Side/Dalla Nation per la Nation/Nation Garage |
| `live-della-nation` | Caption del lunedì (roundup live della settimana) |
| `meta-schedule` | Caricamento e programmazione di un post su Meta Business Suite |

## Come mantenere viva la KB

A fine sessione significativa, chiedi a Claude: *"Aggiorna la KB con quello che abbiamo fatto oggi."* Claude deve:
1. Aggiornare la nota specifica toccata (non l'indice, a meno che cambi la struttura stessa) — la nota contiene la **verità attuale**, non il racconto di come ci si è arrivati.
2. Aggiungere **una riga sola** in [[LOG]] (formato grep-abile, vedi lì) con data e cosa è cambiato — mai un paragrafo. Il "perché"/"come" resta nella nota toccata solo se è un fatto corrente utile, altrimenti resta solo nel log.
3. Se una nota cresce troppo o un argomento merita una nota propria, scorporarla e aggiungerla alla tabella sopra.
4. Per un controllo di salute della KB ("ricontrolla la KB"), delega il lint a un agente Haiku — vedi processo in [[Regole-Operative-Claude]].
