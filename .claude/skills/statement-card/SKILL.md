---
name: statement-card
description: >
  Produce la grafica "statement card" per Spoiler Spotlight, B-Side, Dalla Nation
  per la Nation o Nation Garage: slide singola o carosello con blocchi di testo
  centrati su sfondo brand, generata da tools/spotlight/make_statement_slides.py.
  Usa quando l'utente chiede di preparare uno di questi 4 contenuti ("facciamo il
  B-Side di <banda>", "prepara lo spoiler per <banda>", "contenuto di venerdì/Dalla
  Nation per la Nation", "Nation Garage"), o più in generale una grafica a citazione/
  frase breve nello stile Tribute Nation che non sia un carosello Spotlight a 9 slide
  (quello è la skill `spotlight`, diversa: qui non c'è mai un logo band).
---

# Statement card — Spoiler / B-Side / Dalla Nation / Nation Garage

Questi 4 contenuti condividono lo stesso motore grafico (`make_statement_slides.py`,
già scritto e funzionante — **non riscriverlo**) ma non avevano mai un flusso
formalizzato attorno: si scriveva il copy, si costruiva il JSON a mano, si generava,
si controllava a occhio. Questa skill mette in ordine quei passaggi.

**Principio guida**: il motore fa rispettare automaticamente gli standard di scala
(hook 150-160px, riga secondaria 40-46px — vedi [[Produzione-Grafica-Social]]). Il
tuo lavoro qui è quasi tutto nel copy e nella struttura del config, non nel disegno.

## Passo 1 — Capire quale dei 4 formati serve

| Contenuto | Giorno | Slide | Regola specifica |
|---|---|---|---|
| Spoiler Spotlight | Martedì | 1 | Cita solo l'artista **originale**, mai la tribute (né grafica né caption) — vedi [[Tone-of-Voice]] |
| B-Side | Giovedì | 1 | Formula: dato inaspettato → pivot → chiusura verso la tribute italiana (vedi [[Calendario-Editoriale]]); solo il dato inaspettato va in slide, il resto in caption |
| Dalla Nation per la Nation | Venerdì | 5 (con progress bar) | Domanda/riflessione rivolta ai fan, tono da community non da annuncio |
| Nation Garage | Domenica | N (con progress bar) | Uno spoiler sul futuro di Tribute Nation, un tool/argomento per slide |

Se l'utente non specifica quale, deducilo dal contesto (giorno della settimana target,
o cosa sta chiedendo) — chiedi solo se resta ambiguo.

## Passo 2 — Scrivere il copy prima del JSON

Regola ferma per tutti e 4: **un hook per slide**, non un muro di testo. Se il
contenuto ha più idee (es. B-Side con dato + pivot + chiusura), non impilarle tutte
nella stessa slide con font piccoli — o si sceglie l'idea più forte per la slide e il
resto va in caption, o si spalma su più slide (naturale per Dalla Nation/Nation Garage,
che sono già pensati come carosello).

Altre regole di [[Tone-of-Voice]] che si applicano identiche qui: zero em-dash,
tu/voi, frasi brevi. Se il titolo bebas di una slide potrebbe wrappare su due righe e
contiene una lettera accentata maiuscola che compare più di una volta (es. "PIÙ...PIÙ"),
non è un problema — il motore ha un'interlinea (1.15) che evita che l'accento sparisca
per sovrapposizione con la riga sopra (bug trovato e corretto il 2026-09-02), ma
controlla comunque a occhio il risultato prima di consegnare (Passo 4).

Mostra il copy all'utente prima di generare la grafica, a meno che non l'abbia già
scritto/approvato lui stesso nel messaggio.

## Passo 3 — Costruire il config e generare

Schema completo documentato in testa a `tools/spotlight/make_statement_slides.py`.
In sintesi: un JSON con `output_dir`, opzionale `progress_total` (per i caroselli), e
una lista `slides`, ognuna con `filename`, `header` (il testo rosso in alto, es.
"SPOILER SPOTLIGHT", "B-SIDE", "DALLA NATION PER LA NATION"), opzionale
`progress_index`, e `blocks` — una lista di `{text, font: "bebas"|"dmsans", size,
color: "white"|"red"|"grey", divider_after: true|false}`.

Valori di riferimento (standard fissi, non rivalutare ogni volta):
- Hook bebas breve: **150-160px**.
- Riga secondaria/corpo esteso in dmsans: **40-46px**.
- Un solo hook per slide su Spoiler/B-Side (niente due blocchi bebas impilati).

Salva il JSON nello scratchpad, poi esegui:
```
python tools/spotlight/make_statement_slides.py --config <path>
```

## Passo 4 — Controllo visivo prima di consegnare

Leggi (mostra) ogni slide generata. Controlla in particolare:
- Il testo non è tagliato e non sembra vuoto (se sembra vuoto, il problema quasi
  sempre è la struttura/scala del layout, non serve aggiungere altro testo — vedi
  la lezione strutturale in [[Produzione-Grafica-Social]] sul layout "logo eroe").
- Su titoli bebas multi-riga con lettere accentate ripetute, l'accento è visibile su
  ogni riga.
- Nessun nome di tribute band nello Spoiler (né slide né caption che scriverai dopo).

Itera con l'utente finché non arriva un ok esplicito prima di salvare/programmare il
post (per programmarlo, passa alla skill `meta-schedule`).

## Vedi anche

- [[Produzione-Grafica-Social]] — standard di scala e struttura del formato "statement card"
- [[Tone-of-Voice]] — regole di scrittura, formula B-Side, regola Spoiler
- [[Calendario-Editoriale]] — quando esce ognuno dei 4 contenuti
- `meta-schedule` — per caricare e programmare la grafica prodotta qui
