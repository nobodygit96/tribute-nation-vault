---
tags: [kb, marketing, meta, ads, audit, MARKETING]
aggiornato: 2026-08-26
---

# Ecosistema Meta — Quadro completo, confronto con lo standard, piano d'azione

← [[_CLAUDE-TRIBUTE-NATION|Indice]]

> ⚠️ **Nota di stato — leggere prima di tutto**: questo documento è **solo analisi e proposta**. Nessuna modifica è stata fatta su Meta durante la stesura di questa nota. Ogni azione elencata in [[#4. Piano d'azione proposto (nessuna eseguita)]] richiede **autorizzazione esplicita di Vale, azione per azione**, prima di essere eseguita. Richiesto da Vale il 2026-08-26: "non hai autorizzazioni a fare modifiche o altro, prenditi tutte le note necessarie per farle in un secondo momento SOLO dopo mia autorizzazione specifica".

## 0. Perché questo documento

Dopo la scoperta di un terzo account pubblicitario "fantasma" (2026-08-26, vedi [[Team-Marketing-AI-e-Meta-Ads]]) e di due pixel vuoti mai usati, Vale ha chiesto un quadro complessivo: non più correzioni puntuali una alla volta, ma (1) capire come *dovrebbe* essere strutturato un ecosistema Meta secondo fonti affidabili, (2) confrontarlo con lo stato reale di Tribute Nation, (3) avere un piano chiaro di cosa sistemare, **con la priorità assoluta di non perdere le Pagine** durante qualunque intervento futuro.

## 1. Fonti consultate

- **Meta Business Help Center (fonte primaria/ufficiale)** — ["Best practice per la gestione delle Pagine in Meta Business Suite"](https://www.facebook.com/business/help/2406437459411127?id=420299598837059)
- **Veronica Gentili** (esperta di Meta Ads, già fonte citata in [[Team-Marketing-AI-e-Meta-Ads]] per altri temi) — ["Business Manager: 15 risposte alle domande più frequenti"](https://www.veronicagentili.com/blog/business-manager-faq/)

Entrambe verificate via lettura diretta del contenuto (non solo lo snippet di ricerca).

## 2. Come dovrebbe essere strutturato un ecosistema Meta (sintesi delle fonti)

1. **Un solo portfolio business per l'azienda.** Meta stessa consiglia un solo Business Manager per azienda salvo esigenze di separazione legale/regionale — non è il caso di TN.
2. **Le Pagine Facebook devono essere di proprietà del portfolio business dell'azienda che rappresentano.** Se una Pagina è di proprietà del BM sbagliato, va rimossa da lì e aggiunta al BM corretto (fonte Meta).
3. **Un account Instagram business collegato a una Pagina deve appartenere allo stesso portfolio business della Pagina** — stessa azienda, stesso BM (fonte Meta). ✅ Questo è già il caso di TN.
4. **Partner esterni (agenzie, freelance) vanno aggiunti come "Partner" con accesso a singole risorse, mai come proprietari dell'asset.** L'azienda deve sempre mantenere la proprietà nel proprio portfolio (fonte Meta + Veronica Gentili: "va fatta richiesta di accesso", mai aggiungere risorse del cliente al BM dell'agenzia).
5. **Gli admin del portfolio dovrebbero essere persone stabili e centrali nell'azienda** (titolare o referente fisso), non social media manager temporanei (fonte Veronica Gentili).
6. **Le Pagine Facebook si possono "sganciare" e riassegnare ad altro portfolio in modo relativamente semplice** — a differenza degli account pubblicitari, che sono più rigidi (fonte Veronica Gentili). Punto chiave per la paura di Vale di "perdere le pagine": **il rischio reale di perdita permanente di una Pagina agendo dentro il proprio BM è basso**, il vero rischio noto è perdere il *controllo amministrativo* (es. unico admin che perde l'accesso al proprio account personale), non la Pagina in sé.
7. **Gli account pubblicitari non si possono eliminare, solo disattivare.** Non esiste un modo per "ripulire" un account pubblicitario cancellandolo — al massimo si disattiva o si rinomina (fonte Veronica Gentili). Coerente con la scelta già fatta il 25/08 di rinominare invece di eliminare l'account storico.
8. **Un pixel/dataset per sito, condiviso esplicitamente con l'account pubblicitario che lo usa** — principio già presente in [[Team-Marketing-AI-e-Meta-Ads]] §5, confermato dalle fonti generali sulla struttura extra-Meta (Conversions API, verifica dominio) consultate nella sessione precedente.
9. **Ogni asset dovrebbe avere una singola fonte di verità su chi lo possiede** — asset "orfani" (mai collegati, mai assegnati a nessuno) sono un segnale di configurazione trascurata, non necessariamente pericolosi ma da ripulire per chiarezza.

## 3. Tribute Nation oggi — mappatura rispetto allo standard

| # | Principio standard | Stato TN | Valutazione |
|---|---|---|---|
| 1 | Un solo portfolio business | Un solo BM: `_tribute_nation_` | ✅ A norma |
| 2 | Pagina di proprietà del BM giusto | Pagina Facebook "TributeNation" di proprietà del BM `_tribute_nation_` | ✅ A norma |
| 3 | Instagram nello stesso BM della Pagina | `@_tribute_nation_` di proprietà dello stesso BM | ✅ A norma |
| 3b | Instagram collegato esplicitamente all'account pubblicitario giusto | Collegato a `2429131157229173` il 25/08 (verificata la reversibilità prima di agire) | ✅ A norma (dal 25/08) |
| 4 | Partner esterni solo con accesso, mai proprietà | Nessun partner esterno registrato nel BM (nessuna agenzia terza coinvolta) | ✅ A norma, nessuna azione necessaria |
| 5 | Admin stabili e centrali | Due "persone" nel BM: **"Tribute Nation (tu)"** (Vale, admin reale, accesso completo, attivo) e **"_tribute_nation_"** (identità di sistema auto-creata, "Passkey non attivata", "Nessuna attività") | 🟡 **Da capire meglio** — non è chiaro perché esista una seconda identità amministrativa distinta da Vale, con passkey non attivata. Non risulta una persona fisica reale (nessuna attività mai registrata) — sembra un'identità tecnica generata da Meta, non un secondo essere umano con le chiavi del portfolio. Da chiarire prima di decidere se serve intervenire. |
| 6 | Account pubblicitari puliti, uno solo in uso attivo | 3 account pubblicitari noti: `2429131157229173` (canonico, in uso), `1548998116564966` (rinominato "ARCHIVIATO — non usare" il 25/08), `950481854772862` (personale di Vale, mai finanziato, usato di default solo dal pulsante nativo "Metti in evidenza" di Instagram) | 🟡 **Parzialmente sistemato**. Il secondo è già disinnescato col rinomino. Il terzo non è "nel" BM — è un account del profilo personale di Vale, del tutto fuori dal perimetro del portfolio business: non richiede un'azione sul BM, ma un promemoria operativo (mai usare "Metti in evidenza" nativo). |
| 7 | Account pubblicitari: non eliminabili, solo disattivabili/rinominabili | Coerente con l'azione già fatta (rinomina, non eliminazione) | ✅ Approccio corretto già adottato |
| 8 | Un pixel per sito, condiviso esplicitamente | Pixel reale "TributeNation" (dataset, riceve eventi), condiviso con `2429131157229173` | ✅ A norma per l'uso reale |
| 9 | Nessun asset orfano/duplicato | **2 pixel vuoti trovati il 26/08**: "TributeNation Pixel" (id `28138387815793301`, di proprietà di `_tribute_nation_`, mai ricevuto eventi) e uno chiamato letteralmente "_tribute_nation_" (mai ricevuto eventi) | 🟡 **Rumore da ripulire**, non urgente: sono innocui (non ricevono/non condividono dati), ma vanno tracciati per non confonderli in futuro con quello vero. |
| — | WhatsApp Business | Numero reale attivo (+39 392 891 2701), di proprietà del BM, nome con un refuso ("Trubute Nation") | 🟡 Cosmetico, non strutturale — richiede accesso fisico al telefono per la correzione (non fattibile da qui) |
| — | Dominio verificato | tributenation.it verificato su Meta | ✅ A norma |

**Conclusione della mappatura**: la struttura *di base* (BM unico, Pagina e Instagram nello stesso portfolio, pixel condiviso, dominio verificato) **è già a norma secondo lo standard Meta**. I problemi residui sono tutti di "pulizia" (asset orfani, un nome con refuso, un'identità amministrativa da capire) — **nessuno di questi mette a rischio la proprietà della Pagina o dell'account Instagram**, che sono già nel posto corretto secondo le fonti consultate.

## 4. Piano d'azione proposto (nessuna eseguita)

Ordinate per rischio crescente. **Nessuna di queste azioni è stata eseguita.** Ognuna richiede un sì esplicito di Vale, punto per punto, quando deciderà di procedere.

| # | Azione proposta | Rischio | Reversibile? | Perché farla |
|---|---|---|---|---|
| A | Chiarire cosa sia esattamente l'identità "_tribute_nation_" in Persone (perché ha "Accesso completo: Tutto" ma "Nessuna attività" e passkey non attivata) | Nessuno (è solo lettura/verifica, non una modifica) | — | Prima di toccare qualunque permesso, capire se è un'identità tecnica normale (es. generata dal collegamento Instagram) o qualcosa da rivedere |
| B | Documentare (senza eliminare) i 2 pixel vuoti come "noti e innocui" nella KB, per non riscoprirli da capo in futuro | Nessuno | — | Già fatto in [[Team-Marketing-AI-e-Meta-Ads]] il 26/08 |
| C | Eventualmente rinominare (non eliminare) i 2 pixel vuoti con un'etichetta tipo "NON USARE - vuoto" — stesso approccio già usato per l'account pubblicitario storico | Basso | Sì, il nome si può cambiare di nuovo in qualsiasi momento | Coerenza con la soluzione già adottata e già gradita da Vale per l'account "ARCHIVIATO" |
| D | Correggere il nome WhatsApp "Trubute Nation" → "Tribute Nation" | Nessuno (è un refuso testuale) | Sì | Richiede però accesso fisico al telefono — non eseguibile da remoto, va pianificata come azione di Vale stessa |
| E | Verificare da telefono se il pulsante nativo Instagram "Metti in evidenza" può essere impostato in modo permanente sull'account pubblicitario corretto (`2429131157229173`), oppure se resta sempre da correggere manualmente a ogni sponsorizzata | Nessuno (verifica) | — | Il tentativo di cambiarlo dentro il flusso nativo è fallito con un errore Meta generico il 26/08 — da riprovare in un momento diverso o dal telefono, non necessariamente un problema di configurazione TN |
| F | Aggiungere un secondo admin umano stabile al portfolio (secondo la raccomandazione di Meta/Veronica Gentili su "almeno un admin di backup") | Medio (dà accesso completo a una seconda persona reale) | Sì, un admin si può rimuovere | **Decisa da Vale, 2026-09-03: aggiungerà Daniele a breve.** Non ancora eseguita — quando succede, aggiornare questa riga e la mappatura al punto 5 sopra. |

**Nessuna azione con impatto su Pagina, account Instagram o proprietà del Business Manager è nel piano** — coerente con la priorità assoluta di Vale di non perdere le pagine. Le uniche azioni "di modifica" reale sono cosmetiche/reversibili (rinomina, chiarimento) o richiedono accesso fisico al telefono (fuori portata di questa sessione).

## 4bis. Azioni A, C, E — eseguite il 2026-08-26 con autorizzazione esplicita di Vale

- **A (indagine) — risolta.** L'identità "_tribute_nation_" nelle Persone del BM **non è un umano né un account misterioso**: è la rappresentazione tecnica dell'account Instagram stesso. Verificato sulla pagina dell'asset Instagram (Business Settings → Account Instagram → `@_tribute_nation_`): "Persone assegnate: 2" → **"_tribute_nation_" con Accesso completo** (l'account Instagram che amministra se stesso — meccanismo standard di Meta per account IG collegati) e **"Tribute Nation (You)"** (Vale, accesso parziale: Contenuto/Messaggi/Attività community/Inserzioni/Insights). Il "Passkey non attivata" la rende di fatto dormiente/inutilizzabile per login diretto. Nessuna azione necessaria, nessun rischio.
- **C (rinomina pixel vuoti) — fatta.** Entrambi rinominati da Gestione eventi (icona matita accanto al nome, non da Business Settings): `28138387815793301` → **"NON USARE - vuoto"**, `1045460168263303` → **"NON USARE - vuoto (2)"** (nome diverso richiesto: Meta non accetta due origini dati con nome identico nello stesso portfolio). Il dataset reale "TributeNation" (quello con dati, ID `1034973242374407`) non è stato toccato.
- **E (riprova selezione account nel flusso nativo) — ABBANDONATA, non va più ritentata da browser automatizzato.** Primo tentativo: il picker "Modifica account pubblicitario Facebook" si è aperto regolarmente (stessi 3 account di prima), ma confermare `2429131157229173` è di nuovo fallito con errore generico Meta. Secondo tentativo (stessa sessione, pochi minuti dopo): la finestra del picker questa volta non si è proprio caricata. **Vale ha poi segnalato che ogni tentativo su questo punto le disconnette l'account reale.** Ipotesi più probabile: il browser usato per queste verifiche condivide la stessa sessione autenticata di Vale (limite già noto, non isolata), e i sistemi anti-frode di Meta invalidano la sessione quando rilevano un cambio automatizzato dell'account pubblicitario collegato a un profilo personale. **Conseguenza operativa permanente: il punto E non va più ritentato in autonomia, in nessuna forma, da questo o futuri browser automatizzati.** Se in futuro si vorrà comunque provare a fissare l'account di default nel flusso nativo, va fatto **da Vale in prima persona**, dal proprio telefono/browser normale — mai delegato. Bozze eliminate in sicurezza in entrambi i tentativi, nessuna spesa reale generata. Resta comunque valida la raccomandazione pratica: **usare sempre Gestione inserzioni** (adsmanager.facebook.com) sull'account `2429131157229173` per sponsorizzare, mai il pulsante nativo "Metti in evidenza".

## 5. Risposta diretta alla domanda di Vale: "rischio di perdere le pagine?"

**No, secondo le fonti consultate il rischio è basso.** La Pagina Facebook "TributeNation" e l'account Instagram `@_tribute_nation_` sono già di proprietà del portfolio business corretto (lo stesso BM, `_tribute_nation_`), esattamente come raccomandato da Meta. Le Pagine si possono anche "sganciare" e riassegnare con relativa facilità se mai servisse. Il vero punto di attenzione **non è la struttura degli asset, ma il fatto che oggi solo Vale ha accesso amministrativo reale** — se il suo account personale avesse problemi (blocco, hack, perdita accesso), non ci sarebbe un secondo admin umano pronto a intervenire. Questo è il punto F del piano sopra, da valutare con calma, non un'urgenza.

## Vedi anche

- [[Team-Marketing-AI-e-Meta-Ads]]
- [[Strumenti-e-Risorse]]
