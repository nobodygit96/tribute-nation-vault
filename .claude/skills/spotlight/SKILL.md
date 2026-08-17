---
name: spotlight
description: >
  Produce uno spotlight band intero (articolo, caption, HTML WordPress, 9 slide
  carosello, PDF branded) in autonomia, con solo 3 checkpoint di conferma: quale
  banda, contenuti scritti prima della grafica, pacchetto completo prima del
  caricamento. Salva tutto sul NAS e carica PDF+slide sulla cartella Drive di
  approvazione, restituendo il link finale da girare alla banda. Usa quando
  l'utente dice "facciamo uno spotlight", "prepara lo spotlight di <banda>",
  "/spotlight <banda>", o chiede di produrre il pacchetto spotlight per una band.
---

# Spotlight — produzione end-to-end

Processo definito il 2026-08-17 dopo la prova reale su Frøm Zerø. Segue **esattamente**
gli standard in [[Produzione-Grafica-Social]] e [[Tone-of-Voice]] — questa skill è
l'esecuzione meccanica di quelle regole, non una fonte alternativa. Se KB e questa
skill vanno in conflitto, KB vince: segnalalo e correggi la skill.

**Principio guida**: tra un checkpoint e l'altro lavora in autonomia. Non fermarti per
scelte già coperte dagli standard KB (dimensioni font, colori, struttura pacchetto,
naming file) — applicale direttamente. Fermati SOLO ai 3 checkpoint elencati sotto.

## Checkpoint 1 — Quale banda

Se l'utente ha già indicato la banda (anche come argomento `/spotlight <Banda>`), usa
quella, non richiedere conferma. Altrimenti chiedi.

## Fase A — Raccolta materiale (autonoma)

1. Cerca la cartella banda su NAS: `Z:\TRIBUTE NATION\Band della nation\<Banda>\`.
2. Trova il questionario intake (di solito un PDF email `[SPOTLIGHT] <BANDA>` dentro
   `Spotlight\` o in root) — leggilo per intero, è la fonte primaria per articolo e
   caption. Il questionario ha 10 domande fisse (vedi [[Pipeline-Contenuti-e-Roster]]).
3. **Non fidarti di uno stato "✅ pronto" già scritto in [[Materiali-NAS]] senza
   verificarlo**: apri il file reale dentro `Spotlight\` e controlla che sia davvero un
   pacchetto prodotto (articolo/caption/slide), non solo il PDF dell'email di intake.
4. Recupera foto grezze e logo band dalla root della cartella.
5. Se manca materiale critico (nessuna foto **live** per la cover — foto studio/posate
   non vanno bene per la cover secondo lo standard; questionario introvabile), segnalalo
   subito qui, non aspettare il checkpoint 2.
6. Se il questionario (domanda 8) nomina una tribute band italiana specifica, verifica
   il suo handle Instagram reale con una ricerca web prima di citarlo — mai inventarlo.

## Fase B — Contenuti scritti (autonoma)

Scrivi, in quest'ordine:

- **`{Band}_Articolo.md`**: 1000-1200 parole (**verifica con `wc -w`, non a occhio** —
  una bozza a 803 parole è stata bocciata come "generica"), apertura con aneddoto
  cinematografico, sezioni H2 in title case (prima lettera maiuscola, non tutto
  maiuscolo), citazioni dirette dal questionario come **blockquote veri** (`> testo`),
  sempre introdotte da una frase di contesto prima, mai incollate dentro il paragrafo.
  Zero em-dash (**verifica con grep** `—|–`, zero risultati attesi). Frasi corte ma
  legate da connettivi logici, non frammenti slegati. Chiusura col saluto/frase della
  banda. Non citare/contrapporre generi musicali di altre tribute band a meno che
  l'utente non lo chieda esplicitamente.
- **`{Band}_Articolo_WordPress.html`**: stesso contenuto, `<h1>/<h2>/<p>/<blockquote>`.
- **`{Band}_Caption.md`**: formula in [[Tone-of-Voice]] (hook, presentazione,
  aneddoto, citazione diretta, eventuale tribute rispettata con @handle verificato,
  "Scorri per scoprire la loro storia. 👉", link articolo, hashtag). Emoji incluse.

## Checkpoint 2 — Verifica contenuti scritti

Mostra articolo + caption + html all'utente. Itera sulle correzioni finché non arriva
un ok esplicito. Non procedere alla Fase C prima di quello.

## Fase C — Grafica (autonoma)

1. Verifica che Python + Pillow + numpy + reportlab siano disponibili
   (`python -c "import PIL, numpy, reportlab"`). Se mancano, installa Python via
   `winget install -e --id Python.Python.3.12` e le librerie via pip (dettagli in
   [[Strumenti-e-Risorse]]) — di solito **non serve rifarlo**, controlla prima.
2. Script e font riutilizzabili: `tools/spotlight/make_slides.py` e `make_pdfs.py`
   dentro questa cartella vault (non nella temp di sessione). Non riscriverli da zero:
   sono già parametrizzati e implementano gli standard finali (titoli sempre bianchi,
   font 70/58px titolo, 33px corpo, 26px tag, 22px handle footer, cover logo+nome banda
   ~480px di ingombro totale a centro verticale 72%, grade cover scurimento 0.6/boost
   rosso 1.5/taglio verde 0.55/taglio blu 0.5, vignetta 0.9).
3. Costruisci un `config.json` per `make_slides.py` (schema documentato in testa al
   file) con tag/titoli/body per ogni slide, derivati dalle 10 risposte del
   questionario. Includi la slide "Tribute to Tribute" **solo se** la domanda 8 ha
   dato una risposta con una tribute band italiana specifica — altrimenti saltala,
   non è un elemento fisso (vedi [[Regole-Operative-Claude]]).
4. Esegui `python tools/spotlight/make_slides.py --config <path>` per le slide e
   `python tools/spotlight/make_pdfs.py --articolo ... --caption ... --band "Nome"`
   per i due PDF branded.
5. Controlla visivamente almeno la cover e una slide di contenuto (leggi i PNG
   generati) prima di passare al checkpoint 3 — verifica che il testo non sia tagliato
   e che la foto cover sia effettivamente una foto live.

## Checkpoint 3 — Verifica pacchetto completo

Mostra il pacchetto finale (testi + tutte le slide + PDF) all'utente. Itera sulle
correzioni finché non arriva un ok esplicito. Non caricare nulla prima di quello.

## Fase D — Salvataggio (autonoma)

1. **NAS** (`Z:\TRIBUTE NATION\Band della nation\<Banda>\Spotlight\`): pacchetto
   **completo** — `{Band}_Articolo.md`, `_WordPress.html`, `.pdf`, `{Band}_Caption.md`
   (ready to post, con emoji), `{Band}_Caption.pdf` (senza emoji), `{Band}_Logo.png`,
   tutte le slide, `{Band}_Pacchetto.zip` con tutto dentro. Vedi struttura file esatta
   in [[Produzione-Grafica-Social]].
2. **Google Drive** (solo materiale di revisione per la banda, **mai** i file grezzi
   md/html): crea una sottocartella con il nome della banda dentro
   `G:\Il mio Drive\Approvazioni Spotlight\` (percorso locale sincronizzato — basta
   `mkdir`/copy via PowerShell o Bash, **non serve il browser**: le sottocartelle
   ereditano automaticamente il permesso "chiunque abbia il link" già impostato sulla
   cartella madre). Copiaci dentro solo i PDF (articolo + caption) e le slide PNG.
   Il browser/cambio account (vedi [[Strumenti-e-Risorse]]) serve **solo** se la
   cartella madre non esiste ancora o perde la condivisione — non è un passaggio di
   routine.
3. Aggiorna KB: stato pacchetto in [[Materiali-NAS]] (tabella "Cosa è già pronto"),
   una riga in [[LOG]].
4. Restituisci all'utente il link della cartella madre Drive
   (`https://drive.google.com/drive/folders/1Hv2TevgqdKaEFfNIQulaMWUOLfHWUnnF`) —
   la banda apre quel link e trova la propria sottocartella per nome.

## Vedi anche

- [[Produzione-Grafica-Social]] — standard grafici e struttura pacchetto (fonte di verità)
- [[Tone-of-Voice]] — regole di scrittura
- [[Pipeline-Contenuti-e-Roster]] — questionario a 10 domande
- [[Strumenti-e-Risorse]] — setup Python/Drive, account nobody
- [[Materiali-NAS]] — mappa NAS e regole di salvataggio
