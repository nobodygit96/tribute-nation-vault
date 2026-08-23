---
tags: [kb, marketing, ai, meta, ads, bozza, MARKETING]
aggiornato: 2026-08-23
---

# Team Marketing AI e Meta Ads — Ricerca e Bozza Operativa

← [[_CLAUDE-TRIBUTE-NATION|Indice]]

> ⚠️ **Nota di stato**: questa è una raccolta di idee/indicazioni da fonti esterne (5 video, sessione del 2026-08-23), non ancora tutta verificata o decisa. Non è la "verità compilata" nel senso pieno delle altre note KB — va trattata come backlog da lavorare passo passo. **Integrazione rimandata** con lo sviluppo parallelo di Daniele su agenti/skill (vedi [[Strumenti-e-Risorse]] per l'architettura `.claude/agents` e `.claude/skills` esistente). Fonti: video di Veronica Gentili (Business Manager, Lead Ads, Pixel/Retargeting/Pubblici Personalizzati), Neil Patel (strategia di ricerca multi-canale 2026), Giovanni Beggiato e Grace Leung (team di agenti AI in Claude Code).

## ✅ Verificato da browser il 2026-08-23 (dettagli completi in [[Strumenti-e-Risorse]])

- **Business Manager**: esiste davvero, un solo account pubblicitario "Tribute Nation".
- **5 campagne storiche**, tutte "boost" di post esistenti (follow, visita profilo, interazione, clic sul link) — **nessuna campagna a obiettivo conversione/lead**, spesa totale ≈ €49,85. Nessun uso di retargeting o pubblici personalizzati finora: tutte le campagne hanno usato targeting broad/di default, non pubblici basati su pixel o interazioni pregresse.
- **Pixel Meta: NON installato** (contrariamente a quanto riferito inizialmente) — Gestione eventi non ha nessuna origine dati collegata.
- **Dominio tributenation.it: NON verificato** su Business Manager.

## 🔧 Ancora da verificare

- **Stato reale GA4**: la KB lo segnala come non attivo ([[Strategia-Mercato-e-Sviluppo]]) — richiede login Google separato, non controllato in questa sessione.
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
- [ ] Verificare stato reale GA4
- [ ] **Installare il Pixel Meta** su tributenation.it — non è "verificare", è da fare da zero
- [ ] **Verificare il dominio** tributenation.it via BM — non è "verificare", è da fare da zero
- [ ] Scrivere le regole di routing skill-vs-agente in `CLAUDE.md`
- [ ] Costruire il Pubblico Personalizzato da interazioni FB/IG (365gg, gratis)
- [ ] Formalizzare 2 buyer persona esplicite (band-tipo, locale-tipo) partendo dalla ricerca di mercato già fatta
- [ ] Applicare la mappa impatto/sforzo alle 5 idee di sviluppo non decise in [[Strategia-Mercato-e-Sviluppo]]
- [ ] Costruire l'agente Outreach con disciplina di follow-up sul Venue Tracker
- [ ] Costruire l'agente Trovabilità/SEO per Storia del Rock
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

## Vedi anche

- [[Strategia-Mercato-e-Sviluppo]]
- [[Strumenti-e-Risorse]]
- [[Stato-e-Roadmap]]
- [[Venue-Tracker]]
