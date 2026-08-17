---
tags: [kb, regole, claude, MARKETING]
aggiornato: 2026-08-16
---

# Regole Operative per Claude

← [[_CLAUDE-TRIBUTE-NATION|Indice]]

> Leggere sempre insieme a [[Tone-of-Voice]] a inizio sessione.

## Golden rules tecniche

- Prima CSS puro, poi plugin.
- Evitare framework JS pesanti.
- Niente plugin premium senza conferma.
- 🔧 *Confermare con Vale se queste regole valgono esattamente così.*
- **Regola fondamentale immutabile (Vale, 2026-08-17): prima di pushare un repo condiviso (`TributeNationKB.Cli`, `tribute-nation-kb`, qualunque altro), fare sempre `git pull`/`git fetch` per primo — senza eccezioni.** Motivo concreto: durante questa sessione `TributeNationKB.Cli` era 5 commit indietro, incluse modifiche a `ValidateCommand.cs` stesso — un `tnkb validate` lanciato prima del pull avrebbe potuto dare un risultato non affidabile senza che nessuno se ne accorgesse. Non fidarsi del fatto che "probabilmente non è cambiato niente": verificare sempre con `git fetch` + confronto (`git log HEAD..origin/<branch> --oneline`) prima di push, e se è un progetto compilato (come `TributeNationKB.Cli`), ribuildare dopo il pull prima di usare il binario.

## Anonimato (critica, fissa)

Non nominare mai Tribute Nation, il sito o l'handle Instagram in contesti legati al nome reale di Vale (es. LinkedIn). "Nobody" è la persona pubblica condivisa dei due co-fondatori (Vale e Daniele): mai un nome/cognome/titolo reale in nessun contenuto pubblico, indipendentemente da chi ha scritto quel contenuto. Dettagli in [[Identita-e-Ruolo]].

## Copy e testi pubblici

Italiano, tono rock/diretto come da [[Tone-of-Voice]], firmati "Nobody" quando è outreach o comunicazione pubblica (vedi [[Identita-e-Ruolo]]).

## Slide carosello — note tecniche

- Le emoji non renderizzano in Pillow → usare sostituti grafici (freccette, triangoli).
- I caratteri accentati italiani richiedono unicode escape nei heredoc Python.
- I caratteri cirillici (es. Я) richiedono FreeSansBold (`/usr/share/fonts/truetype/freefont/FreeSansBold.ttf`) perché Bebas Neue non supporta il cirillico.
- Trasparenza logo: mascherare i pixel dove r,g,b < 40.
- Specifiche complete (canoni social, script Python, struttura pacchetto) in [[Produzione-Grafica-Social]].

## Cosa fare a inizio sessione

Leggere [[_CLAUDE-TRIBUTE-NATION|l'indice]] e le note rilevanti, internalizzare ruolo/tono/regole, e chiedere a Vale solo le informazioni davvero nuove non già coperte nella KB.

## Manutenzione della KB (pattern "LLM Wiki" di Karpathy)

Questa KB segue il pattern Index → Wiki → Log per la memoria persistente degli agenti AI ([gist originale di Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), aprile 2026). Tre regole per restare token-efficient nel tempo:

1. **Le note (wiki) contengono la verità compilata attuale** — fatti correnti, non narrazione di sessione. La cronologia di *come* si è arrivati a un fatto vive solo in [[LOG]], non duplicata dentro la nota.
2. **[[LOG]] è append-only e terso**: una riga per entry con prefisso coerente (`- **data** [tag] testo breve. [[Note]].`), mai un paragrafo — deve restare grep-abile. Se un'entry supera 2-3 righe, il dettaglio va spostato nella nota pertinente, non lasciato nel log.
3. **Lint periodico**: quando richiesto ("ricontrolla la KB"), delega un agente Haiku a cercare — link `[[...]]` rotti, note non in indice (o viceversa), frontmatter mancante/data implausibile, contraddizioni tra note (stesso fatto raccontato in modo diverso), marker 🔧/"verificare con Vale" ormai risolti altrove, ridondanza (stesso contenuto ripetuto invece di un rimando), pagine orfane senza link in entrata, cross-link mancanti tra note tematicamente collegate. Applica i fix meccanici (link mancanti, date frontmatter) direttamente; per le contraddizioni che richiedono una scelta, segnala e chiedi a Vale invece di decidere da solo.

## Errori noti da non ripetere

- RATS = tribute RATM, **non** Ghost.
- KoRnea = tribute Korn, **non** Ghost.
- Spotlight e articolo sono un solo processo, due output — non trattarli come fasi separate.
- La domenica è dedicata agli aggiornamenti del progetto TN, non a contenuti band o post di interazione.
- La slide "Band rispettate" si chiama ora **"Tribute to Tribute"** (deciso da Vale il 2026-08-16, sul pacchetto di prova Frøm Zerø — tag in inglese, sostituisce il vecchio nome italiano da questa data in poi). Non è un punto fisso in ogni spotlight (es. Again ce l'ha): può essere gestita diversamente a seconda di cosa emerge dal questionario/intervista — non un elemento obbligatorio da forzare se il materiale non la giustifica. Il pacchetto Wonderwall (verificato 2026-08-16) infatti non ne ha una.
- Flammen: correzione applicata nel CMS WordPress ("tribute Rammstein tedeschi" dopo "i GGG" — rimosso "tedeschi"). Verificata sul sito (vedi [[Pipeline-Contenuti-e-Roster]]).

## Vedi anche

- [[Tone-of-Voice]]
- [[Identita-Visiva]]
- [[Produzione-Grafica-Social]]
- [[Pipeline-Contenuti-e-Roster]]
