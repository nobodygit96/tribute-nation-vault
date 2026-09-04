---
tags: [kb, marketing, ai, meta, ads, bozza, MARKETING]
aggiornato: 2026-08-26
---

# Team Marketing AI e Meta Ads — Ricerca e Bozza Operativa

← [[_CLAUDE-TRIBUTE-NATION|Indice]]

> ⚠️ **Nota di stato**: questa è una raccolta di idee/indicazioni da fonti esterne (5 video, sessione del 2026-08-23), non ancora tutta verificata o decisa. Non è la "verità compilata" nel senso pieno delle altre note KB — va trattata come backlog da lavorare passo passo. **Integrazione rimandata** con lo sviluppo parallelo di Daniele su agenti/skill (vedi [[Strumenti-e-Risorse]] per l'architettura `.claude/agents` e `.claude/skills` esistente). Fonti: video di Veronica Gentili (Business Manager, Lead Ads, Pixel/Retargeting/Pubblici Personalizzati), Neil Patel (strategia di ricerca multi-canale 2026), Giovanni Beggiato e Grace Leung (team di agenti AI in Claude Code).

## ✅ Verificato/risolto da browser il 2026-08-23 (dettagli completi in [[Strumenti-e-Risorse]])

- **Business Manager**: esiste davvero. **Causa reale del problema "pixel non selezionabile nei Pubblici Personalizzati"**: l'account pubblicitario `2429131157229173` (quello usato per tutte le campagne reali) non era mai stato un asset del BM `_tribute_nation_` — era amministrato solo a livello di profilo personale di Vale. Confermato con tre controlli indipendenti, poi **migrato nel BM** ("reclamato", azione irreversibile) e **ricollegato al dataset reale** (essere nello stesso BM non basta, va condiviso esplicitamente asset per asset). Verificato funzionante creando un Pubblico Personalizzato di prova ("Visitatori sito web 180gg - TributeNation") dal dataset reale.
- **11 campagne storiche in totale tra i due account** (5 su `2429131157229173`, 6 su `1548998116564966` — quest'ultime scoperte solo il 2026-08-25, prima si credeva quell'account non fosse mai stato usato), tutte "boost"/prospecting, **nessuna a obiettivo conversione/lead**, spesa totale reale ≈ €97,13. Nessun uso di vere liste di Pubblico Personalizzato/retargeting: anche la campagna chiamata "REMARKETING" usava targeting Advantage+ automatico su un pubblico ampio, non un pubblico basato su pixel o interazioni pregresse. Dettaglio completo in [[Strumenti-e-Risorse]].
- **Pixel Meta: installato e funzionante** — dataset "TributeNation" attivo, riceve eventi in tempo reale, ora collegato anche all'account pubblicitario usato per le campagne.
- **Dominio tributenation.it: Verificato** su Business Manager (meta-tag inserito via Code Snippet sul sito, revisionato da `tn-deploy-reviewer` prima dell'attivazione, cache svuotata, scraping Meta forzato via Sharing Debugger Tool).
- **Dubbio di Vale sul 2026-08-25: "account pubblicitario sbagliato collegato a Instagram" — non confermato, ma ha portato a una correzione importante.** Controllato da più angolazioni: (1) Impostazioni business → Account Instagram: un solo account (`@_tribute_nation_`), unica risorsa collegata era la Pagina Facebook "TributeNation", nessun account pubblicitario elencato; (2) "Risorse collegate" di entrambi gli account pubblicitari: nessuno dei due mostrava risorse collegate nel grafo asset del BM; (3) anteprima reale di tutte le inserzioni Instagram-native storiche su entrambi gli account (comprese quelle scoperte su `1548998116564966`): identità corretta ovunque, sempre `TributeNation`/`@_tribute_nation_`. Origine del dubbio, chiarita da Vale: provando a sponsorizzare dall'app Instagram, l'account offerto sembra "nuovo". Controllando `1548998116564966` per la prima volta in Gestione inserzioni (prima solo ipotizzato "mai usato" dalle impostazioni business, mai verificato) è emerso che **ha davvero avuto una campagna reale** (€47,28, conclusa il 09/08/2026) — quindi nessuno dei due account era genuinamente "nuovo".
- **Consolidamento deciso da Vale il 2026-08-25**: la situazione non era ordinata (due account pubblicitari con storie separate, uno migrato in ritardo, un pixel relitto isolato, nessun collegamento diretto Instagram↔account pubblicitario). Deciso di usare **`2429131157229173` come account pubblicitario canonico** da qui in avanti. **Azioni eseguite**: (1) verificato che collegare risorse in Business Settings è reversibile (pulsante "Scollega" sempre presente, nessun avviso di irreversibilità), poi collegato esplicitamente `@_tribute_nation_` a `2429131157229173` tramite "Risorse collegate" → ora 2 risorse collegate all'account Instagram: Pagina Facebook TributeNation + account pubblicitario `2429131157229173`; (2) **`1548998116564966` rinominato in "ARCHIVIATO - Tribute Nation (non usare)"** (campo "Nome dell'account pubblicitario", via il menu "..." → "Modifica" in Business Settings) per eliminare il rischio concreto di selezionarlo per sbaglio — era ancora pienamente attivo e selezionabile nonostante il consolidamento. Non risolve da solo il "sembra nuovo" nell'app Instagram (quella scelta resta lato app, non nel grafo BM) ma chiude il rischio di scambio manuale in Gestione inserzioni.
- **Account WhatsApp — verificato il 2026-08-25, esiste e funziona: non toccare la configurazione.** Business Account "Trubute Nation" (refuso nel nome, non corretto) di proprietà del BM, con un numero reale collegato e attivo: **+39 392 891 2701**, stato "Collegato", qualità "Alta". Profilo business non completato (non verificato, nessun indirizzo/valuta/metodo di pagamento) ma il numero funziona comunque. Nessuna scheda "Risorse collegate" disponibile per gli account WhatsApp in questa UI: non partecipano allo stesso grafo asset di Pagine/Instagram/account pubblicitari/dataset — quindi la domanda "è collegato a un account pubblicitario" non si applica nello stesso modo. Non ancora documentato altrove in KB dove/come viene usato questo numero nel lavoro quotidiano — da chiarire con Vale se serve.
- **Domanda di Vale il 2026-08-26: "in Business Settings → Persone → Assegna risorse, il pixel e WhatsApp non risultano assegnati, perché?"** Verificato da browser: la persona/identità aperta in quel momento era **`_tribute_nation_`** (un'identità di sistema creata automaticamente, con "Nessuna attività", distinta dall'utente reale di Vale "Tribute Nation (tu)"), che ha solo Pagina Facebook + account Instagram esplicitamente assegnati — mai Pixel o WhatsApp. Non è un problema: entrambe le identità hanno "Accesso completo: Tutto" a livello di portfolio, e il pixel reale (dataset "TributeNation") è comunque **attivo e riceve eventi**, assegnato al vero account di Vale. **Scoperta collaterale però reale**: in "Dataset e pixel" esistono **3 elementi**, non 1 — solo **"TributeNation"** (Meta Pixel + Conversions API) riceve dati; **"TributeNation Pixel"** (ID `28138387815793301`, di proprietà proprio di `_tribute_nation_`) e un terzo chiamato **"_tribute_nation_"** risultano entrambi "Nessun dato collegato", cioè pixel vuoti/mai installati da nessuna parte — verosimilmente creati automaticamente in qualche flusso passato (collegamento IG o simile), non dannosi ma ulteriore "rumore" nella BM coerente con la situazione già segnalata da Vale il 25/08. Non ancora deciso se ripulirli (richiede conferma esplicita prima di eliminare un asset).
- **Mistero del "sembra un account nuovo" nell'app Instagram — risolto il 2026-08-26.** Usando il pulsante nativo "Metti in evidenza post" su Instagram (non Gestione inserzioni) è comparso un **terzo account pubblicitario mai visto prima, `950481854772862`**, intestato "Valeria Mann", **senza alcun metodo di pagamento** e senza i campi obbligatori UE "Chi è l'inserzionista/Chi paga" compilati — dettagli coerenti con un account mai realmente usato. Causa reale: il pulsante nativo di Instagram **non risolve l'account pubblicitario dal grafo della Business Manager**, ma da un meccanismo separato legato al profilo Facebook personale collegato all'account Instagram (dialog di sistema: "Controlla l'account pubblicitario Facebook che stai usando" → mostra "Valeria Mann" come account di default). Il picker di quella dialog conferma tutti e 3 gli account visti finora nella sessione: *Valeria Mann* (950481854772862, no pagamento), *2429131157229173* (corretto, PayPal collegato), *ARCHIVIATO - Tribute Nation (non usare)*. Ho provato a selezionare `2429131157229173` come account di default per questo flusso: la conferma è fallita con un errore generico Meta ("Si è verificato un problema da parte nostra") — sembra un bug/instabilità del flusso nativo stesso, non della configurazione BM. **Non è un fantasma/asset sconosciuto da investigare oltre**: è semplicemente l'account ads di default del profilo personale di Vale, mai finanziato. Bozza eliminata correttamente per uscire in sicurezza dal flusso. **Raccomandazione operativa**: non usare il pulsante nativo "Metti in evidenza"/"Promuovi" di Instagram per sponsorizzare — usare sempre Gestione inserzioni (adsmanager.facebook.com) sull'account canonico `2429131157229173`, dove la selezione dell'account è esplicita e affidabile.

## 🔧 Ancora da verificare

- **GA4, GTM, Search Console**: nessuno dei tre attivo sul sito (confermato da browser). Roadmap e checklist operativa pronte in nota dedicata: [[Integrazione-Google-GTM-GA4-Search-Console]] — in attesa di accessi/decisioni da Vale.
- A che punto è lo sviluppo di Daniele sul team di agenti marketing (vedi nota progetto in memoria Claude, non in questa KB).

> **Lezione da questa sessione**: un'informazione riferita a voce ("BM e Pixel ci sono già") si è rivelata solo parzialmente vera alla verifica diretta (BM sì, Pixel no). Buona pratica confermata: verificare da browser prima di pianificare su stati non controllati direttamente, specialmente quando cambiano le priorità a valle.

## Campagna recruiting band via sponsorizzazione (decisa il 2026-09-02, da impostare la sera stessa)

Prima inserzione vera pianificata per Tribute Nation. Obiettivo: far conoscere il progetto a tribute band che non lo conoscono ancora e portarle a candidarsi tramite "Entra nella Nation" — parla solo del livello gratuito, i pacchetti a pagamento non sono ancora nel copy pubblico (vedi [[Servizi-a-Pagamento-Band]]).

- **Obiettivo campagna:** Traffico (clic al link), non Notorietà/Messaggi.
- **Budget:** €4/giorno, **durata 14 giorni** (~€56 totali). Confermato da Vale.
- **Account pubblicitario:** `2429131157229173` (canonico, PayPal collegato), da usare **solo** via Gestione inserzioni (adsmanager.facebook.com) — mai il pulsante nativo "Metti in evidenza"/"Promuovi" di Instagram, che porta all'account personale di Vale senza pagamento collegato (vedi sezione sopra, 2026-08-26).
- **Formati creativi**, in `GRAFICHE POST\recruiting_band_02_09_26\`: `recruiting_band_single.png` (1080x1080, feed) e `recruiting_band_story.png` (1080x1920, Storie/Reel — copre anche il placement WhatsApp Status che riusa lo stesso asset). Hook: "Ogni tribute band in Italia ha un posto qui."
- **Targeting:** admin di Pagine Facebook incrociato con interessi musicali (cover band, strumenti, generi rock/metal/pop), età 25-55, geografia Italia intera. Confermato da Vale.
- **Copy diviso nei campi Meta**: testo primario = caption lunga (lista servizi con emoji, vedi caption approvata); titolo breve = "Entra nella Nation, gratis"; descrizione = "Pagina, Spotlight, calendario e bot: tutto gratis."
- **UTM: deciso di non usarli per questa campagna (2026-09-02)**. GA4/GTM/Search Console non sono ancora attivi sul sito (vedi sezione "Ancora da verificare" sopra), quindi nessuno strumento leggerebbe i parametri UTM oggi — il link di destinazione resta pulito. Da riconsiderare quando GA4 sarà installato: a quel punto tracciare le campagne a pagamento separatamente dal traffico organico diventa un lavoro sensato da fare.
- **🔧 Da chiudere la sera dell'impostazione**: scelta del CTA button ("Registrati" vs "Scopri di più").
- **Nota di funnel (non ancora confermata con Daniele)**: il link punta alla pagina "Entra nella Nation" (spiega i servizi), non direttamente alla registrazione — scelta pensata per traffico freddo da inserzione, che ha bisogno di un passaggio di "riscaldamento" prima di chiedere la creazione di un account.

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
- [x] ~~Collegare Instagram all'account pubblicitario canonico~~ — fatto 2026-08-25, verificata la reversibilità prima di agire
- [x] ~~Verificare se WhatsApp Business è collegato~~ — fatto 2026-08-25: sì, numero reale attivo, non toccato
- [x] ~~Rinominare l'account pubblicitario storico per evitare scambi~~ — fatto 2026-08-25: `1548998116564966` → "ARCHIVIATO - Tribute Nation (non usare)"
- [ ] Correggere il nome WhatsApp "Trubute Nation" → "Tribute Nation" — **va fatto dal telefono** (app WhatsApp Business, Impostazioni → Strumenti aziendali → Profilo aziendale), il controllo "Modifica" in Meta Business Manager è disabilitato per questo tipo di account (verificato via DOM, `aria-disabled="true"`)
- [ ] Decidere se/quando completare il profilo WhatsApp Business (azienda non verificata, nessun indirizzo/valuta) — non urgente, il numero funziona comunque
- [x] ~~Verificare da telefono quale account pubblicitario offre di default l'app Instagram quando si sponsorizza un post~~ — risolto 2026-08-26: è l'account del profilo personale di Vale (`950481854772862`), mai finanziato. Non usare il pulsante nativo "Metti in evidenza", usare sempre Gestione inserzioni.
- [x] ~~Chiarire l'identità "_tribute_nation_" nelle Persone del BM (azione A)~~ — fatto 2026-08-26: è l'account Instagram stesso, non una persona. Vedi [[Ecosistema-Meta-Audit-e-Piano]] §4bis.
- [x] ~~Rinominare i 2 pixel vuoti per chiarezza (azione C)~~ — fatto 2026-08-26: "NON USARE - vuoto" e "NON USARE - vuoto (2)".
- [x] ~~Riprovare a fissare l'account pubblicitario di default nel flusso nativo Instagram (azione E)~~ — **ABBANDONATA definitivamente 2026-08-26**: ogni tentativo disconnette l'account reale di Vale (sospetta rilevazione anti-frode Meta sulla sessione condivisa del browser). Non va più ritentata da browser automatizzato, in nessuna forma futura. Vedi [[Ecosistema-Meta-Audit-e-Piano]] §4bis.
- [ ] **In attesa di autorizzazione di Vale** — azioni D (correggere nome WhatsApp, serve il telefono) e F (valutare un secondo admin di backup) in [[Ecosistema-Meta-Audit-e-Piano]] §4
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
- [ ] Decidere se/quando caricare il database Brevo come Custom Audience (richiede consenso già raccolto) — 🔧 bloccato finché Brevo stesso non è attivo, vedi correzione sotto

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
- Retargeting (ads a pagamento) vs remarketing (email via Brevo) — distinguere sempre i due nella pianificazione. **Correzione 2026-09-04**: Brevo non è ancora attivo per TN (nessun account, nessun invio reale finora), contrariamente a quanto scritto qui prima. Il "remarketing via Brevo" era una previsione, non uno stato attuale.
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

- [[Ecosistema-Meta-Audit-e-Piano]] — quadro completo confrontato con fonti affidabili + piano d'azione (nessuna azione eseguita, in attesa di autorizzazione)
- [[Report-Portfolio-Sponsorizzate-Meta]] — report campagne per portfolio personale di Vale
- [[Strategia-Mercato-e-Sviluppo]]
- [[Strumenti-e-Risorse]]
- [[Stato-e-Roadmap]]
- [[Venue-Tracker]]
- [[Integrazione-Google-GTM-GA4-Search-Console]]
- [[Tone-of-Voice]]
- [[Identita-Visiva]]
- [[Pipeline-Contenuti-e-Roster]]
