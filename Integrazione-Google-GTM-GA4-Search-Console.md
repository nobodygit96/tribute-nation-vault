---
tags: [kb, marketing, google, ga4, gtm, search-console, MARKETING]
aggiornato: 2026-08-23
---

# Integrazione Google — GTM, GA4, Search Console

← [[_CLAUDE-TRIBUTE-NATION|Indice]]

> ⏸️ **Da riprendere**: roadmap e checklist pronte, lavoro non ancora iniziato. Bloccato in attesa di decisioni/accessi da Vale (vedi sotto). Fonti: ricerca web del 2026-08-23 su best practice GTM/GA4/Search Console 2026.

## Stato di partenza (verificato da browser il 2026-08-23)

Controllato l'HTML live di tributenation.it: **nessun tag Google presente** — niente GTM, niente GA4/gtag.js, nessun plugin "Site Kit by Google" installato. Coerente con quanto già in [[Stato-e-Roadmap]] e [[Funzionalita-Sito-e-Area-Riservata]] ("GA4 non ancora attivo"). Si parte da zero su tutti e tre i fronti.

## Sequenza corretta

1. Creare la proprietà **GA4**
2. Creare il container **GTM**
3. Installare **GTM** sul sito (un solo snippet, in `<head>`)
4. Configurare il **tag GA4 dentro GTM** (Google Tag, trigger "Initialization – All Pages")
5. Verificare/collegare **Search Console** — tramite GTM stesso, non un metodo di verifica separato

⚠️ **Regola d'oro, stesso errore già fatto con il pixel Meta duplicato**: mai installare GA4 sia via GTM sia via codice diretto/plugin contemporaneamente — causa doppio conteggio di pageview ed eventi.

## Decisioni/accessi che servono da Vale prima di procedere

1. **Quale account Google usare** — serve un account dedicato a Tribute Nation (non l'account personale di Vale), per non legare l'accesso a una singola persona per sempre. Nessun accesso Google disponibile in sessione: a differenza di Meta, qui serve login esplicito di Vale nel browser o le credenziali.
2. **Site Kit by Google (plugin) vs. installazione manuale via Code Snippet** — Site Kit è ufficiale e più comodo (dashboard, OAuth guidato) ma aggiunge un plugin in più su un sito che ha già 24 snippet relitti mai ripuliti (segnalato da `tnkb brief`, KB tecnica di Daniele). Preferenza di Claude: Code Snippet manuale, stesso schema pulito usato per la verifica dominio Meta — ma è reversibile, decide Vale.
3. **Consenso cookie (iubenda)** — il sito ha già un banner iubenda attivo (hook `wp_head`). I tag Google vanno collegati al **Consent Mode v2** di Google, altrimenti si traccia prima del consenso (problema GDPR concreto). Da verificare se il piano iubenda sottoscritto include l'integrazione nativa — richiede accesso al pannello iubenda.

## Checklist operativa

| # | Passo | Chi | Dipende da |
|---|---|---|---|
| 1 | Decidere quale account Google usare | Vale | — |
| 2 | Decidere Site Kit vs. Code Snippet manuale | Vale | — |
| 3 | Controllare il piano iubenda per supporto Google Consent Mode v2 | Claude (con accesso al pannello iubenda) | Login iubenda |
| 4 | Creare la proprietà GA4 | Claude (con login Google in sessione) | Punto 1 |
| 5 | Creare il container GTM | Claude | Punto 4 |
| 6 | Installare lo snippet GTM sul sito | Claude | Punto 5, punto 2 |
| 7 | Configurare il tag GA4 dentro GTM (trigger "Initialization – All Pages") | Claude | Punto 6 |
| 8 | Collegare il Consent Mode v2 (se iubenda lo supporta) prima di pubblicare | Claude | Punto 3 |
| 9 | Pubblicare il container GTM ("Submit") | Claude, con conferma esplicita di Vale (azione visibile in produzione) | Punto 8 |
| 10 | Aggiungere la proprietà su Search Console, verificare **via GTM** (non un metodo separato) | Claude | Punto 9 |
| 11 | Collegare Search Console a GA4 (admin GA4 → "Collegamenti Search Console") | Claude | Punti 4, 10 |
| 12 | Test finale: eventi in tempo reale su GA4 + dominio verificato su Search Console | Claude | Punto 11 |
| 13 | Aggiornare [[Stato-e-Roadmap]] e [[Funzionalita-Sito-e-Area-Riservata]] togliendo "GA4 non attivo" | Claude | Punto 12 |

**Prossimo passo per riprendere**: login Google di Vale nel browser + risposta ai punti 1-2 sopra.

## Vedi anche

- [[Team-Marketing-AI-e-Meta-Ads]]
- [[Stato-e-Roadmap]]
- [[Strumenti-e-Risorse]]
