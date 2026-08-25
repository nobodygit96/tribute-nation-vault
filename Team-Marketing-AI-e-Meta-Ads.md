---
tags: [kb, marketing, ai, meta, ads, bozza, MARKETING]
aggiornato: 2026-08-25
---

# Team Marketing AI e Meta Ads — Ricerca e Bozza Operativa

← [[_CLAUDE-TRIBUTE-NATION|Indice]]

> ⚠️ **Nota di stato**: questa è una raccolta di idee/indicazioni da fonti esterne (5 video, sessione del 2026-08-23), non ancora tutta verificata o decisa. Non è la "verità compilata" nel senso pieno delle altre note KB — va trattata come backlog da lavorare passo passo. **Integrazione rimandata** con lo sviluppo parallelo di Daniele su agenti/skill (vedi [[Strumenti-e-Risorse]] per l'architettura `.claude/agents` e `.claude/skills` esistente). Fonti: video di Veronica Gentili (Business Manager, Lead Ads, Pixel/Retargeting/Pubblici Personalizzati), Neil Patel (strategia di ricerca multi-canale 2026), Giovanni Beggiato e Grace Leung (team di agenti AI in Claude Code).

## ✅ Verificato/risolto da browser il 2026-08-23 (dettagli completi in [[Strumenti-e-Risorse]])

- **Business Manager**: esiste davvero. **Causa reale del problema "pixel non selezionabile nei Pubblici Personalizzati"**: l'account pubblicitario `2429131157229173` (quello usato per tutte le campagne reali) non era mai stato un asset del BM `_tribute_nation_` — era amministrato solo a livello di profilo personale di Vale. Confermato con tre controlli indipendenti, poi **migrato nel BM** ("reclamato", azione irreversibile) e **ricollegato al dataset reale** (essere nello stesso BM non basta, va condiviso esplicitamente asset per asset). Verificato funzionante creando un Pubblico Personalizzato di prova ("Visitatori sito web 180gg - TributeNation") dal dataset reale.
- **5 campagne storiche**, tutte "boost" di post esistenti (follow, visita profilo, interazione, clic sul link) — **nessuna campagna a obiettivo conversione/lead**, spesa totale ≈ €49,85. Nessun uso di retargeting o pubblici personalizzati finora: tutte le campagne hanno usato targeting broad/di default, non pubblici basati su pixel o interazioni pregresse.
- **Pixel Meta: installato e funzionante** — dataset "TributeNation" attivo, riceve eventi in tempo reale, ora collegato anche all'account pubblicitario usato per le campagne.
- **Dominio tributenation.it: Verificato** su Business Manager (meta-tag inserito via Code Snippet sul sito, revisionato da `tn-deploy-reviewer` prima dell'attivazione, cache svuotata, scraping Meta forzato via Sharing Debugger Tool).
- **Dubbio di Vale sul 2026-08-25: "account pubblicitario sbagliato collegato a Instagram" — non confermato.** Controllato da tre angolazioni: (1) Impostazioni business → Account Instagram: un solo account (`@_tribute_nation_`), unica risorsa collegata è la Pagina Facebook "TributeNation", nessun account pubblicitario elencato; (2) "Risorse collegate" di entrambi gli account pubblicitari (`1548998116564966` e `2429131157229173`): nessuno dei due mostra risorse collegate, quindi nessun legame diretto Instagram↔account pubblicitario nel grafo asset del BM; (3) anteprima reale delle due inserzioni "Post di Instagram" storiche (Gestione inserzioni, account `2429131157229173`): entrambe mostrano correttamente l'identità `TributeNation`/`@_tribute_nation_`. Nessun errore trovato nei punti controllati — se il dubbio nasce da una schermata specifica (es. impostazioni native dell'app Instagram, non controllabili da qui), va indicata per un controllo mirato.

## 🔧 Ancora da verificare

- **GA4, GTM, Search Console**: nessuno dei tre attivo sul sito (confermato da browser). Roadmap e checklist operativa pronte in nota dedicata: [[Integrazione-Google-GTM-GA4-Search-Console]] — in attesa di accessi/decisioni da Vale.
- A che punto è lo sviluppo di Daniele sul team di agenti marketing (vedi nota progetto in memoria Claude, non in questa KB).

> **Lezione da questa sessione**: un'informazione riferita a voce ("BM e Pixel ci sono già") si è rivelata solo parzialmente vera alla verifica diretta (BM sì, Pixel no). Buona pratica confermata: verificare da browser prima di pianificare su stati non controllati direttamente, specialmente quando cambiano le priorità a valle.

## 1. Team marketing AI dedicato

Metodo (da Grace Leung): mappare i task ricorrenti reali → una skill per workflow → raggruppare skill non sovrapposte in agenti dedicati → routing esplicito in `CLAUDE.md`.

Agenti proposti, mappati sui task reali di TN (non un template da agenzia generica):

| Agente | Possiede | Stato |
|---|---|---|
| **Content/Spotlight** | Pipeline questionario→articolo→carosello→caption | Esiste già come skill `/spotlight` |
| **Outreach** | Follow-up sistematico su Band Tracker + Venue Tracker (56+ locali fermi a "Da contattare") | Da costruire |
| **Trovabilità/SEO** | Storia del Rock e articoli come risposta a domande reali, monitoraggio menzioni AI | Da costruire |
| **Metriche/Reporting** | Sostituisce lo snapshot manuale mensile in [[Stato-e-Roadmap]] con dati reali | Da costruire |
| **Media Buyer** | Attivo solo su campagne a pagamento (già esistono, vedi sopra — rivalutare priorità) | Da costruire/rivalutare |

**Passo tecnico mancante, comune a tutto**: regole di routing skill-vs-agente esplicite in `CLAUDE.md` — oggi non ci sono, e sbloccano tutto il resto.

**Metodo di costruzione skill (reference-based)**: partire da materiale reale già approvato (es. captions passate confermate da Vale), non da zero — lo stesso modo in cui è nata `/spotlight`.

## 2. Altre IA a supporto dei subagenti

| Sub-agente | Tool/IA esterna | Per cosa |
|---|---|---|
| Trovabilità/SEO | AnswerThePublic.com | Domande reali digitate da fan/band |
| Trovabilità/SEO | Ubersuggest.com | Verificare se ChatGPT/AI Overview citano già TN |
| Creatività social | Nano Banana (Gemini via MCP) | Alternativa/complemento a Canva+Pillow per varianti creative generate via prompt |
| Metriche/Reporting | Meta Graph API / Business Suite | Dati Insights reali invece di trascrizione manuale |

Principio trasversale: **mai dati/numeri inventati** — qualunque agente che tocchi competitor o metriche usa fonti verificate (WebSearch/API reali), mai stime a occhio.

## 3. To-do list di implementazione

- [x] ~~Verificare dettagli reali di BM, Pixel e campagne Meta già fatte~~ — fatto 2026-08-23, vedi [[Strumenti-e-Risorse]]
- [x] ~~Migrare l'account pubblicitario nel BM e ricollegare il dataset~~ — fatto 2026-08-23
- [x] ~~Verificare il dominio tributenation.it via BM~~ — fatto 2026-08-23
- [ ] Procedere con l'integrazione Google (GTM, GA4, Search Console) — roadmap pronta in [[Integrazione-Google-GTM-GA4-Search-Console]], serve login/decisioni di Vale
- [ ] Scrivere le regole di routing skill-vs-agente in `CLAUDE.md`
- [ ] Costruire il Pubblico Personalizzato da interazioni FB/IG (365gg, gratis)
- [ ] Formalizzare 2 buyer persona esplicite (band-tipo, locale-tipo) partendo dalla ricerca di mercato già fatta
- [ ] Applicare la mappa impatto/sforzo alle 5 idee di sviluppo non decise in [[Strategia-Mercato-e-Sviluppo]]
- [ ] Costruire l'agente Outreach con disciplina di follow-up sul Venue Tracker (Fase 3, dopo conferma con Daniele)
- [ ] Formalizzare la checklist di brand compliance (§7) prima di qualunque agente che pubblica (Fase 1)
- [ ] Costruire l'agente Trovabilità/SEO partendo dai topic di §8 (Fase 2)
- [ ] Costruire l'agente Metriche/Reporting (Fase 4, bloccato su GA4 attivo)
- [ ] Coordinarsi con Daniele sullo sviluppo parallelo del team agenti
- [ ] Decidere se/quando caricare il database Brevo come Custom Audience (richiede consenso già raccolto)

## 4. Altre idee e applicazioni concrete

- Spotlight come contenuto-madre multi-formato (sito+IG+eventuale video), non contenuti scollegati.
- Outreach come leva di visibilità AI (brand mentions), non solo business diretto.
- Video/Reel dello spotlight: le AI citano contenuti video più di altri formati.
- Lead magnet per i locali (se si deciderà il pacchetto a pagamento): mini-report gratuito tipo "quante persone cercano tribute band nella tua zona".
- Finestra di retargeting da testare per il settore eventi live: probabilmente breve (legata alla data del concerto), non i 180gg standard.
- Coerenza del messaggio su ogni canale (da Neil Patel) — TN ha già una regola forte di coerenza tono/persona "Nobody"; l'agente Trovabilità/SEO potrebbe anche controllare che sito/social/outreach non si contraddicano mai.

## 5. Istruzioni per la gestione Meta

- Un pixel per brand/sito — verificare che sia unico e non condiviso.
- Non mischiare pubblici di valore diverso (visitatori sito vs interazione pagina) in uno stesso Custom Audience, salvo necessità di aggregare per la size minima.
- GDPR: consenso esplicito obbligatorio per caricare un database contatti come Custom Audience — verificare che Brevo copra anche questo uso, non solo l'email.
- Budget minimo: si può testare anche con 5€/giorno su pubblici piccoli.
- Retargeting (ads a pagamento) vs remarketing (email via Brevo, già in uso) — distinguere sempre i due nella pianificazione.
- Non essere aggressivi con target sensibili (es. locali in difficoltà economica) — testare il tono prima di scalare.

## 6. Roadmap operativa e gap analysis (ricerca del 2026-08-24)

### Cosa dicono le fonti 2026 (oltre ai 2 video già citati in §1)

- **Prima si documenta il brand, poi si costruisce l'agente**: il processo standard parte da una documentazione di identità/tono già scritta, prima di dare in pasto qualunque cosa a un agente. TN questo passo lo ha già fatto: [[Tone-of-Voice]] e [[Identita-Visiva]] esistono, sono già la "knowledge base del brand" richiesta — non c'è da inventare nulla, solo collegarle esplicitamente a ogni agente/skill che genera contenuto pubblico.
- **Una brand voice utile è specifica e "contrastiva"**: dice anche cosa NON è, non solo cosa è, con esempi concreti. [[Tone-of-Voice]] ha già questa forma nelle "Regole ferme" (zero em-dash, zero bullet nelle caption, zero frasi AI-sounding) — più vicino a un guardrail azionabile che a un semplice mood board, buon punto di partenza.
- **Serve un passo di verifica/compliance prima della pubblicazione**, non solo un buon prompt iniziale: il contenuto generato va confrontato contro le regole del brand come step esplicito, non fidandosi che il modello "si ricordi" il tono per tutta la sessione.
- **Su Claude Code specificamente**: `CLAUDE.md` + skill è già il meccanismo di orchestrazione, non serve un orchestratore esterno — conferma la strada già proposta in §1 (routing skill-vs-agente). I subagenti supportano ora anche l'annidamento (un agente che ne lancia altri, fino a profondità 5) — utile in futuro se un agente Content dovesse delegare a un sub-check di brand compliance invece di fare tutto in un prompt monolitico.
- **Meglio pochi strumenti ben integrati che tanti scollegati** (3-5 con scambio dati pulito battono una collezione di tool isolati) — coerente con quanto già segnalato da `tnkb brief` sul sito (24 snippet relitti mai ripuliti): vale la stessa logica per il team di agenti, non solo per il codice.

### Gap analysis — cosa manca per procedere, e da dove recuperarlo

| Cosa manca | Serve da | Blocca |
|---|---|---|
| Regole di routing skill-vs-agente in `CLAUDE.md` | Scrittura diretta — criterio già chiaro: comando meccanico → skill, giudizio ripetuto → agente | Tutto il resto: senza routing esplicito un nuovo agente/skill rischia di sovrapporsi o non attivarsi mai |
| Un passo di "brand compliance check" esplicito, oggi implicito (Vale rilegge a occhio) | Formalizzare le "Regole ferme" di [[Tone-of-Voice]] come checklist eseguibile (§7 sotto) | Qualunque agente che pubblica contenuto senza supervisione — oggi va bene perché Vale rilegge sempre, non scala se il volume aumenta |
| Stato dello sviluppo parallelo di Daniele | Chiedere direttamente a Daniele | Formalizzare in KB una struttura definitiva, per non duplicare o contraddire scelte già sue |
| Accesso GA4/Search Console per l'agente Metriche/Reporting | Login Google di Vale — stessa dipendenza di [[Integrazione-Google-GTM-GA4-Search-Console]] | L'agente Metriche/Reporting non ha dati reali su cui lavorare finché GA4 non è attivo |
| Decisione di Vale su quale agente costruire per primo | Priorità esplicita di Vale | L'ordine delle fasi sotto è una proposta, non è ancora decisa |

### Come propongo di gestirlo (fasi, non tutto insieme)

1. **Fase 0 — routing in `CLAUDE.md`.** Prerequisito tecnico di tutto il resto, zero dipendenze esterne.
2. **Fase 1 — guardrail di brand come checklist esplicita** (§7). Rischio più basso, protegge la cosa non negoziabile del progetto (il tono di voce), serve a ogni agente successivo — conviene farla prima di costruire qualunque agente che pubblica.
3. **Fase 2 — agente Trovabilità/SEO.** Meno dipendenze esterne (non serve GA4, non serve coordinarsi con Daniele), output verificabile subito: i topic di §8 sono il primo banco di prova concreto.
4. **Fase 3 — agente Outreach** sul Venue Tracker, una volta chiarito con Daniele se si sovrappone al suo sviluppo.
5. **Fase 4 — agente Metriche/Reporting**, bloccato su GA4 attivo (dipendenza diretta da [[Integrazione-Google-GTM-GA4-Search-Console]]).
6. **Media Buyer resta in fondo**: campagne esistenti minime (€49,85 totali), non è priorità finché il volume non lo giustifica.

Un agente alla volta, validato su output reale prima di passare al successivo — stesso principio già confermato per `/spotlight` (costruita da materiale reale approvato, non da zero).

## 7. Guardrail di brand per gli agenti (non negoziabili)

Le "Regole ferme" di [[Tone-of-Voice]], trasformate in checklist che qualunque agente/skill che genera contenuto pubblico deve rispettare prima della consegna a Vale:

- [ ] Zero em-dash (—) nel testo finale
- [ ] Zero bullet point nelle caption
- [ ] Nessuna frase "AI-sounding" (frammenti slegati, tono istituzionale, liste informative al posto di narrazione)
- [ ] Citazioni solo da materiale intervista reale, mai inventate o parafrasate come dirette
- [ ] Palette/font rispettati in ogni asset grafico ([[Identita-Visiva]]): `#0A0A0A`/`#CC2200`/bianco, Bebas Neue + DM Sans Variable, 🤘 come firma
- [ ] Struttura articolo rispettata quando applicabile (apertura aneddotica, H2 non tutto maiuscolo, chiusura con saluto/frase della band)
- [ ] "Tu/voi", mai il "lei" istituzionale

Non sostituisce la rilettura di Vale — è un primo filtro meccanico prima che un contenuto le arrivi, pensato per la Fase 1 sopra.

## 8. Topic per nuovi articoli — "Storia del Rock" (bozza da validare)

> Non ancora un contenuto attivo nel [[Calendario-Editoriale]]: è il criterio editoriale di [[Strategia-Mercato-e-Sviluppo]] ("Storia del Rock come risposta a domande reali", da Neil Patel) applicato a proposte concrete. Nessuno di questi articoli esiste ancora — sono candidati, da scrivere solo con fonti verificate, mai a memoria.

Topic scelti per collegarsi a tribute band già nel roster TN (spotlight pubblicati o pagina sito), per permettere link interni reali invece di articoli isolati:

| Domanda reale (stile ricerca) | Genere/contesto | Collegamento roster TN |
|---|---|---|
| Perché i Nirvana e il grunge di Seattle hanno cambiato il rock per sempre? | Grunge | Genere coperto da 4 band nel roster |
| Qual è la differenza tra hard rock, heavy metal e nu metal? | Metal/Nu Metal | KoRnea (Korn), Disasterpiece (Slipknot) |
| Perché i Rage Against the Machine restano un riferimento politico nel rock? | Rock politico/Alternative | RATS |
| Come sono nati gli Alice in Chains e perché il grunge non è solo Nirvana? | Grunge | Again |
| Qual è la storia dei Black Sabbath e perché sono i padri del metal? | Heavy Metal | Mr. Crowley (Ozzy/Black Sabbath) |
| Perché il Britpop degli anni '90 è ancora amato oggi (Oasis vs Blur)? | Britpop | Supersonic Show / Wonderwall (Oasis) |
| Cos'è successo ai Guns N' Roses tra Use Your Illusion e la reunion? | Hard Rock | Paradise Roses |
| Perché i Rammstein dividono il pubblico tra spettacolo e controversia? | Industrial Metal | Flammen |
| Come è nato il nu metal e perché Korn e Limp Bizkit restano rilevanti? | Nu Metal | KoRnea, KissMyStarfish |
| Cosa rende Soundgarden e il progetto Temple of the Dog unici nella storia grunge? | Grunge | Outshined |
| Perché i Ghost mescolano teatro, horror e metal (e perché funziona)? | Metal teatrale | Eponymous |
| Qual è la storia degli U2 e perché restano la band stadio per eccellenza? | Rock/Stadium | Sound of Existence |
| Come si è evoluto il metalcore/post-hardcore con band come A Day To Remember? | Metalcore | 2nd Sucks |
| Il Britpop revival di oggi: cosa lo lega davvero agli anni '90? | Britpop | Wonderwall (pagina sito, no spotlight ancora) |
| Perché il "nuovo corso" dei Bring Me the Horizon divide i fan metalcore? | Metalcore/Alternative | Sleepwalkers (citata in 2nd Sucks) |
| Come si organizza una serata/contest tribute band in Italia (guida pratica)? | Servizio/Locali | Non lega a una band, lega ai [[Venue-Tracker]] — utile per outreach locali |

Nota di processo: ogni articolo va scritto solo dopo verifica reale delle fonti storiche (mai a memoria del modello) — stesso principio già fermo per il §2 di questa nota ("mai dati/numeri inventati").

## Vedi anche

- [[Strategia-Mercato-e-Sviluppo]]
- [[Strumenti-e-Risorse]]
- [[Stato-e-Roadmap]]
- [[Venue-Tracker]]
- [[Integrazione-Google-GTM-GA4-Search-Console]]
- [[Tone-of-Voice]]
- [[Identita-Visiva]]
- [[Pipeline-Contenuti-e-Roster]]
