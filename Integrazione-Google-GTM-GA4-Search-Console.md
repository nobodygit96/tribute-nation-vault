---
tags: [kb, marketing, google, ga4, gtm, search-console, MARKETING]
aggiornato: 2026-09-10
---

# Integrazione Google — GTM, GA4, Search Console

← [[_CLAUDE-TRIBUTE-NATION|Indice]]

> ▶️ **In corso**: GA4, GTM e il tag di consenso iubenda sono tutti configurati il 10/09, in bozza nel workspace GTM — nessun tag pubblicato/live ancora. Resta la revisione congiunta con Daniele prima di pubblicare, e un blocco separato sulla verifica Search Console (probabile cache/firewall lato hosting). Fonti: ricerca web del 2026-08-23 su best practice GTM/GA4/Search Console 2026.

## Stato tecnico al 2026-09-10 (fine sessione)

- **Account Google**: `nobody.tribute.nation@gmail.com`, confermato attivo nel browser prima di ogni creazione.
- **GA4**: account "Tribute Nation", proprietà "tributenation.it", stream web `https://www.tributenation.it` — Stream ID `15750199694`, **Measurement ID `G-1Z0SX6TN4B`**.
- **GTM**: account "Tribute Nation" (ID `6376035146`), container "tributenation.it" (ID `263699478`) — **container ID `GTM-N8NZV4BZ`**.
- **Snippet base GTM sul sito**: Code Snippet WordPress #111 ("GTM - Container base (head + body)"), hook `wp_head` (priorità 1) + `wp_body_open`, **salvato e ATTIVO**. Revisionato da `tn-deploy-reviewer` (nessuna modifica richiesta). Verificato via fetch diretto della homepage: script `<head>` e `<noscript>` `<body>` presenti, status 200, nessun errore PHP. Verificato anche che non esisteva già nessun altro container GTM/tag `gtag.js` sul sito (nessun doppione). **Il container è vuoto (0 tag pubblicati): questo snippet da solo non traccia nulla**, è innocuo.
- **Tag GA4 dentro GTM**: creato ("GA4 - Configurazione base", tipo "Tag Google", ID misurazione `G-1Z0SX6TN4B`, trigger "Initialization - All Pages") — **salvato nel workspace GTM, NON pubblicato**. Ha il supporto nativo a Google Consent Mode v2 built-in (non serve configurazione aggiuntiva per questo).
- **Gate di consenso — COMPLETATO (in bozza)**: trovato un **template ufficiale iubenda per GTM** ("iubenda Privacy Controls and Cookie Solution", aggiornato 17/06/2026, nella Galleria modelli della community di GTM) che risolve il problema alla radice — legge lo stato di consenso reale di iubenda dal sito e lo inoltra a Google Consent Mode v2 (tutti gli 8 segnali: ad_storage, analytics_storage, ad_user_data, ad_personalization, ecc.), con default "Denied" su tutte e 4 le categorie finché l'utente non interagisce col banner. Il tentativo di stamattina si era fermato sul campo obbligatorio "CS configuration" (serve l'oggetto `_iub.csConfiguration` dalla dashboard iubenda.com). L'agente di Daniele ha recuperato il valore esatto dalla dashboard del progetto (siteId `4577327`, cookiePolicyId `62195901`) e l'ho incollato carattere per carattere (verificato via confronto stringa esatto, 332/332 caratteri) nel tag **"iubenda - Consent Mode v2"**, trigger "Consent Initialization - All Pages" (gira prima di ogni altro tag, come richiesto). Il campo "CS language configuration" è stato lasciato vuoto/separato come indicato. **Tag salvato nel workspace GTM, NON pubblicato** — resta in bozza in attesa di revisione congiunta con Daniele prima di premere "Invia" sul container.
- **Questa scoperta cambia il quadro rispetto al 09/09**: non serve più necessariamente il pattern "gate server-side lato PHP" ipotizzato per i pixel pubblicitari — il template ufficiale iubenda fa la stessa cosa in modo nativo e supportato, per QUALSIASI tag futuro instradato tramite GTM (non solo GA4). Resta comunque un problema separato per Meta/TikTok Pixel finché non vengono anch'essi migrati dentro GTM (oggi Meta è un plugin a parte, TikTok è un Code Snippet a parte — nessuno dei due passa da GTM).
- **Task aperto sul Monitor per Daniele** (10/09, priorità Media): "Serve accesso a iubenda.com per completare il tag Consent Mode v2 in GTM" — contiene link alla documentazione ufficiale, cosa manca esattamente e dove trovarlo.
- **Nuovo blocco trovato, non risolto**: proprietà Search Console creata (`https://www.tributenation.it`, prefisso URL) ma **verifica fallita 3 volte** con due metodi diversi (Google Tag Manager: "snippet in posizione sbagliata"; Tag HTML via meta tag Code Snippet #112: "impossibile trovare il meta tag"), nonostante conferma diretta via fetch che sia lo script GTM sia il meta tag sono presenti e corretti nell'head della pagina live. Svuotata la cache di Aruba HiSpeed Cache dal suo pannello dedicato (non solo il "Cancella cache" generico della admin bar) senza risolvere. Sospetto principale: un layer di cache o firewall lato hosting (Aruba HiSpeed Cache o Really Simple Security, entrambi attivi sul sito) che serve al verificatore di Google una risposta diversa da quella vista in ogni mio test diretto. Non approfondito oltre per evitare tentativi a vuoto — richiede o un semplice retry dopo propagazione cache, o l'intervento di Daniele sui log/regole del firewall.

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

1. ~~**Quale account Google usare**~~ — **deciso il 2026-09-10: `nobody.tribute.nation@gmail.com`** (lo stesso già usato per Google Drive e per la registrazione di TikTok For Business), coerente con la regola di non legare gli account di brand al profilo personale di Vale.
2. **Site Kit by Google (plugin) vs. installazione manuale via Code Snippet** — Site Kit è ufficiale e più comodo (dashboard, OAuth guidato) ma aggiunge un plugin in più su un sito che ha già 24 snippet relitti mai ripuliti (segnalato da `tnkb brief`, KB tecnica di Daniele). Preferenza di Claude: Code Snippet manuale, stesso schema pulito usato per la verifica dominio Meta — ma è reversibile, decide Vale.
3. ~~**Consenso cookie (iubenda) — bloccante**~~ — **risolto il 2026-09-10**: template ufficiale iubenda per GTM configurato con i dati reali del progetto (da Daniele), tag "iubenda - Consent Mode v2" salvato in bozza nel workspace GTM. Resta solo la revisione congiunta con Daniele prima di pubblicare.

## Checklist operativa

| # | Passo | Chi | Dipende da |
|---|---|---|---|
| 1 | ~~Decidere quale account Google usare~~ — `nobody.tribute.nation@gmail.com` | Vale | ✅ fatto 2026-09-10 |
| 2 | ~~Decidere Site Kit vs. Code Snippet manuale~~ — Code Snippet manuale | Vale | ✅ fatto 2026-09-10 |
| 3 | ~~Creare la proprietà GA4~~ — `G-1Z0SX6TN4B` | Claude | ✅ fatto 2026-09-10 |
| 4 | ~~Creare il container GTM~~ — `GTM-N8NZV4BZ` | Claude | ✅ fatto 2026-09-10 |
| 5 | ~~Installare lo snippet GTM sul sito~~ — Code Snippet #111, attivo | Claude | ✅ fatto 2026-09-10 |
| 6 | ~~Configurare il tag GA4 dentro GTM~~ — creato, non pubblicato | Claude | ✅ fatto 2026-09-10 |
| 7 | ~~Ottenere da iubenda.com l'oggetto `_iub.csConfiguration` e completare il tag~~ — tag "iubenda - Consent Mode v2" salvato in bozza | Daniele (dato) + Claude (configurazione) | ✅ fatto 2026-09-10 |
| 8 | Revisione congiunta con Daniele + test in Anteprima GTM (nessun hit prima dell'interazione col banner) | Claude + Daniele | Punto 7 |
| 9 | Pubblicare il container GTM ("Invia") | Claude, con conferma esplicita di Vale (azione visibile in produzione) | Punto 8 |
| 10 | Aggiungere la proprietà su Search Console, verificare **via GTM** (non un metodo separato) | Claude | Punto 9 |
| 11 | Collegare Search Console a GA4 (admin GA4 → "Collegamenti Search Console") | Claude | Punto 10 |
| 12 | Test finale: eventi in tempo reale su GA4 + dominio verificato su Search Console | Claude | Punto 11 |
| 13 | Aggiornare [[Stato-e-Roadmap]] e [[Funzionalita-Sito-e-Area-Riservata]] togliendo "GA4 non attivo" | Claude | Punto 12 |

**Prossimo passo per riprendere**: sessione congiunta con Daniele per rivedere il tag "iubenda - Consent Mode v2" in Anteprima GTM prima di pubblicare il container, e risolvere in parallelo il blocco di verifica Search Console (vedi sopra).

## Vedi anche

- [[Team-Marketing-AI-e-Meta-Ads]]
- [[Stato-e-Roadmap]]
- [[Strumenti-e-Risorse]]
