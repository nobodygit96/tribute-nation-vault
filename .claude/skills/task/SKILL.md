---
name: task
description: >
  Apre un TASK sulla TN Board del Monitor interno (http://192.168.1.87:4173/#/roadmap),
  la coda di lavoro tecnico che Daniele e le sessioni Claude/terminale eseguono davvero
  (repo Sito, TributeNationKB.Cli, TributeNationBot, Monitor, KB). Usa quando l'utente
  dice "apri un task sul Monitor", "mettilo sulla board", "creiamo un TN per questo", o
  descrive un problema/una funzione da sviluppare e chiede di tracciarla lì. NON è la
  stessa cosa di un messaggio 1-a-1 a Daniele sul Monitor (quello è per comunicazioni,
  non per lavoro tecnico da eseguire — se l'utente vuole solo avvisarlo di qualcosa,
  usa la sezione Messaggi del Monitor, non questa skill).
---

# Aprire un task sulla TN Board del Monitor

La TN Board (`#/roadmap`) è una coda di lavoro reale: i task che ci finiscono vengono
ripresi da sessioni Claude o dal terminale, con revisione automatica e deploy — non è
una bacheca decorativa. Per questo un task va scritto con lo stesso livello di
precisione di un requisito tecnico, non come una nota veloce.

## Prima di scrivere il task

Se la richiesta dell'utente è vaga (un nome di funzione, un problema accennato senza
dettagli), **non inventare i requisiti** — chiedi di descriverla con la stessa
precisione con cui verrebbe scritta per uno sviluppatore che parte da zero: cosa deve
fare, a cosa si ispira/cosa deve replicare se esiste già un pattern simile sul sito,
quali campi/sezioni servono. Un task vago genera lavoro sprecato quando la sessione
che lo riprende deve fermarsi a chiedere chiarimenti che si potevano dare subito.

Controlla anche la KB (`_CLAUDE-TRIBUTE-NATION.md` e le note collegate) per contesto
già noto sull'argomento, prima di scrivere la nota del task.

## Passo 1 — Aprire il Monitor

Il Monitor gira su `http://192.168.1.87:4173`, in LAN. Usa **Claude in Chrome**
(`mcp__claude-in-chrome__*`), non il Browser pane sandboxato — quest'ultimo restituisce
"Autenticazione richiesta" perché non ha la sessione già loggata dell'utente, mentre
Chrome reale sì. Se i tool `claude-in-chrome` sono deferred, caricali con ToolSearch
prima (`select:mcp__claude-in-chrome__tabs_context_mcp,...`).

Naviga a `http://192.168.1.87:4173/#/roadmap`.

Per le regole complete (formato, stati, dipendenze, ciclo di vita) la fonte di verità
tecnica è `reference/tn-board.md` nella KB di Daniele
(`C:\Users\vmann\Documents\Tribute Nation KB\reference\tn-board.md`, 1900+ righe) — non
duplicarla qui, ma consultala se un caso non è coperto da questa skill (es. task che
dipende da un altro, piano complesso da decomporre in più TN, catena sequenziale/
"ombrello"). Quello che segue è solo il sottoinsieme che serve per il caso comune:
un task singolo, aperto dall'interfaccia web.

## Passo 2 — Compilare "Nuovo task"

Clicca "Nuovo task" (in alto a destra della board). Il modal ha:
- **Titolo**: breve, specifico, riconoscibile a colpo d'occhio in una board con altri
  150+ task. **Max 90 caratteri** (limite tecnico di `deriveTitle`, `tn-board.md`
  §"Titolo in testa alla voce") — oltre, il titolo può comparire grezzo con asterischi
  invece che in grassetto. Punta a 60 per stare larghi.
- **Nota (opzionale ma da riempire sempre per un task funzionale)**: qui va tutta la
  precisione della richiesta originale — non un riassunto. Se l'utente ha dato una
  spec strutturata (sezioni, campi, comportamenti), riportala organizzata con le stesse
  sezioni (dashes, etichette maiuscole), non compressa in un paragrafo unico nel testo
  che scrivi — ma sappi che **l'app appiattisce comunque tutti gli a-capo in un unico
  paragrafo continuo quando salva** (verificato dal vivo su TN-163, 10/09/2026: nessun
  a-capo sopravvive, nemmeno tra sezioni). Non è un bug da correggere: è voluto, il
  parser della board scarta in silenzio una riga senza indentazione (`tn-board.md`
  §"Formato di una voce"). Struttura comunque il testo con trattini/maiuscole per
  leggibilità nel flusso continuo, ma non aspettarti che i ritorni a capo restino visibili.
- **Priorità**: Alta/Media/Bassa/Standby. Criterio (`tn-board.md` §"Priorità"): **quanto
  blocca altro lavoro o quanto è rischioso lasciarlo aperto**, non quanto è grande il
  task — un task piccolo ma bloccante è Alta, uno grande ma isolato può restare Bassa.
  Media è il default ragionevole per una nuova funzionalità non urgente.
- **Repo (per la revisione automatica)**: seleziona quello coerente col lavoro. Instrada
  il revisore automatico: `Sito` → `tn-deploy-reviewer`; `TributeNationKB.Cli` /
  `TributeNationBot` / `Monitor` → `tn-code-reviewer`; `KB` → nessuna revisione
  automatica (resta a revisione umana, di proposito). "Nessuno" salta la revisione —
  non lasciarlo su "Nessuno" se il task produrrà codice.

**Creator/assignee (convenzione fissata il 10/09/2026, "regola imprescindibile" secondo
`tn-board.md` §"Creator e assignee")**: ogni task nuovo dovrebbe portare un tag
`[creator:X]` — nickname fissati: `Bleed` = Daniele, `Scaloppina` = Valeria — di default
secondo la postazione da cui viene aperto (`Scaloppina` dal PC di Vale). **Il modal web
"Nuovo task"/"Modifica" verificato il 10/09/2026 non espone ancora questo campo**: non
provare ad aggiungerlo scrivendolo a mano nel testo, non è verificato che il parser
della board lo riconosca da lì (la via pensata per questo è `tnkb roadmap create
--creator <nick>` lato CLI, non la UI). Se manca, non è un errore tuo — segnalalo
all'utente/a Daniele come gap noto, non provare a forzarlo.

## Passo 3 — Inviare e VERIFICARE (non fidarti del solo modal che si chiude)

Clicca "Aggiungi alla Roadmap". **Il modal che si chiude non è prova che il task sia
stato creato** — in sessione reale (2026-09-10) il primo tentativo è fallito in
silenzio: nessun errore visibile, modal chiuso normalmente, ma il task non è comparso
da nessuna parte e i contatori delle colonne non sono cambiati. Il secondo tentativo,
identico, è riuscito.

Verifica sempre dopo l'invio:
1. Controlla il contatore "Aperti · N" in alto — deve essere aumentato di 1 rispetto a
   prima dell'invio (annotalo prima di inviare).
2. Scorri fino in cima alla colonna della priorità scelta e conferma che il task
   compaia come primo card, con titolo e ID `TN-NNN` assegnato.
3. Se manca, **rifai da capo il Passo 2** invece di presumere un problema di rete — è
   il pattern già osservato.

Non usare la barra di ricerca globale in alto ("Cerca ovunque…") per verificare: è un
command palette diverso, cerca altrove e non aiuta a confermare. Usa la barra di
ricerca interna alla board ("Cerca… (f)", sotto il titolo "TN BOARD") oppure lo scroll
diretto della colonna.

## Passo 4 — Aggiornare la KB

Registra la richiesta nella nota pertinente (es. [[Stato-e-Roadmap]] sotto "On the
horizon" per una nuova funzionalità) con l'ID del task (`TN-NNN`) assegnato, e una riga
in [[LOG]]. La TN Board è la fonte di verità tecnica di Daniele — questa KB resta quella
di marketing/contenuti, quindi basta un riferimento, non la duplicazione della spec
completa (quella vive nel task stesso).

## Passo 5 — Pulizia

Chiudi la tab Chrome aperta per questa sessione (`tabs_close_mcp`) prima di finire,
come per ogni tab aperta da una skill.

## Differenza con un messaggio a Daniele

Se l'obiettivo è solo avvisare Daniele di qualcosa (serve un suo accesso, una sua
decisione, una segnalazione puntuale) e non tracciare lavoro tecnico da eseguire, usa
invece la sezione **Messaggi** del Monitor (`#/t/messages`, "Una persona specifica" →
cerca il suo nome — occhio a eventuali account duplicati/test, verifica email ed età
registrazione prima di scegliere il destinatario). Un messaggio 1-a-1 è cancellabile
dopo l'invio; un broadcast a tutti gli iscritti no — rileggi sempre prima di inviare, e
chiedi conferma esplicita all'utente prima di premere "Invia" per qualunque messaggio,
è un'azione visibile ad altri.

## Vedi anche

- [[Stato-e-Roadmap]]
- [[Funzionalita-Sito-e-Area-Riservata]] — cos'è il Monitor, a cosa serve
- [[Strumenti-e-Risorse]]
- `Tribute Nation KB/reference/tn-board.md` (KB tecnica di Daniele, non questa) — regole
  complete: formato riga, stati (🔧/🔑/👀/🚀), dipendenze fra task, piani complessi/
  "ombrelli" sequenziali, creator/assignee
