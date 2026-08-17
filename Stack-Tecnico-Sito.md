---
tags: [kb, wordpress, stack-tecnico, todo, MARKETING, WEB]
aggiornato: 2026-08-16
---

# Stack Tecnico del Sito

← [[_CLAUDE-TRIBUTE-NATION|Indice]]

> Copre più sotto-aspetti del sito WordPress (stack, pagine, admin, CSS, eventi). Sono raggruppati qui perché per ora sono per lo più 🔧 **DA COMPLETARE** — se crescono di contenuto, scorporarli in note proprie e aggiungerle all'indice.

## Stack noto

- **CMS:** WordPress
- **Page builder:** Elementor
- **Tema:** Astra
- **SEO:** Yoast SEO
- **Hosting:** Aruba

## Stack da completare 🔧

- Plugin principali installati (calendario eventi, form, slider, backup, altro)
- Plugin installati ma da **non** usare (conflitti, deprecati)
- Cache attiva? Quale?

## Architettura pagine

> Verificato il 2026-08-16 (vedi [[Stato-e-Roadmap]] e [[Pipeline-Contenuti-e-Roster]] per lo stato dei contenuti). Elenco delle pagine principali online, non ancora un inventario completo del sito.

| Pagina | URL | Funzione |
|---|---|---|
| Home | `/` | Landing, teaser band/blog/calendario/mappa |
| Blog (spotlight) | `/blog/` (paginato `/blog/page/N/`) | Elenco articoli Spotlight |
| Articolo spotlight | slug piatto, es. `/flammen-il-fuoco-che-i-rammstein-hanno-acceso-a-roma/` | Non annidato sotto `/blog/` — slug diretto sulla root |
| Directory band | `/area-band/` | 47 pagine band, filtri per genere e artista tributato |
| Directory venue | `/area-venue/` | Elenco locali pubblicati (1 al 2026-08-16) |
| Hub onboarding | `/entra-nella-nation/` | 3 form: Pagina sito, Spotlight, Calendario date |
| Calendario eventi | `/events/` | Date live della Nation |
| Login | `/accedi/` | Accesso area riservata (fan/band/venue) |
| Contatti | `/contatti-generale/` | Form contatto generale |
| Form fan | `/fan-form/` | Iscrizione fan |

Pagine con funzionalità speciali (CPT, slider), pagine da eliminare 🔧 *ancora da raccogliere.*

## Accesso admin 🔧

- URL pannello admin (di solito `/wp-admin/`)
- Altri URL frequenti (lista eventi, customizer CSS, form…)

## CSS e personalizzazioni 🔧

- Dove va il CSS personalizzato (Customizer, child theme, plugin)
- CSS attivi da documentare
- Pattern/regole particolari (es. "usa sempre !important", selettori da non toccare)

## Calendario eventi sito (concerti) 🔧

Il calendario editoriale Notion ([[Strumenti-e-Risorse]]) pianifica i *contenuti*, non è il calendario eventi del sito. Se il sito usa un plugin come The Events Calendar, documentare:
- Plugin usato
- Timezone WordPress
- Formato data preferito (es. "12 Giugno 2026" vs "June 12, 2026")
- Orario di default eventi
- Venue/luoghi già salvati
- Template standard per il titolo evento

## Vedi anche

- [[Regole-Operative-Claude]] — golden rules tecniche (es. CSS puro prima dei plugin)
