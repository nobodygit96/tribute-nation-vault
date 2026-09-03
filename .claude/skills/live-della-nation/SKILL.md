---
name: live-della-nation
description: >
  Scrive la caption settimanale "Live della Nation" (contenuto del lunedì: roundup
  di tutti i live della settimana di qualunque band della Nation), dato un elenco di
  date/locali/band. Usa quando l'utente chiede "scrivimi la caption del lunedì",
  "live della settimana", "Live della Nation", o incolla un elenco di date/locali/
  band chiedendo di trasformarlo in un post. Non genera la grafica (il carosello lo
  prepara Vale a mano su Canva) — solo il testo della caption.
---

# Caption "Live della Nation" (lunedì)

Roundup di **tutti** i live della settimana di qualunque band della Nation, non lo
spotlight di una singola band — errore di pianificazione già fatto in passato (vedi
[[Calendario-Editoriale]], "Correzioni del 2026-06-21"). Se ti viene chiesto di
trattarlo come contenuto mono-band, è quasi certamente un fraintendimento: chiedi
conferma prima di procedere così.

## Input che ti serve

Un elenco di live della settimana: data, città, locale/evento, band, artista
tributato. Se manca qualcosa (es. il locale di una data), chiedilo invece di
inventarlo o ometterlo silenziosamente — meglio un buco visibile che un dato falso.

## Struttura della caption (dagli esempi reali confermati)

1. **Apertura**: hook breve con emoji calendario/data, tono "si riparte, ecco dove
   suona la Nation questa settimana" — non ripetere la stessa frase ogni settimana
   parola per parola, varia mantenendo il tono.
2. **Corpo, organizzato per giorno** (tipicamente venerdì/sabato/domenica, ma segui
   i giorni reali dell'elenco): una frase per giorno che elenca le band di quel
   giorno con città e locale, collegando le band con una frase che scorre invece di
   un elenco puntato secco (zero bullet point nelle caption, regola ferma di
   [[Tone-of-Voice]]). Ogni band va taggata col suo handle Instagram quando
   disponibile — **mai inventare un handle**: se non sei sicuro che sia corretto
   (verificalo con una ricerca web se necessario) o l'utente non te l'ha dato, usa
   un placeholder tra parentesi quadre tipo `[@nomeband]` e segnalalo esplicitamente,
   così chi pubblica lo compila prima di andare live.
3. **Chiusura**: menziona il bot Telegram di Tribute Nation (nelle storie in
   evidenza) come modo per trovare il live più vicino, e una riga di CTA per le band
   che vogliono le proprie date nel post della settimana successiva ("Scrivici").

## Tono

Narrativo, non un bollettino: "Venerdì è la sera più piena: [@banda1] accende Roma
sulle note dei [Artista1], mentre [@banda2] fa esplodere [Genere] a [Città]..." è il
registro giusto, non "Venerdì: Banda1 - Roma - Locale1 / Banda2 - Città2 - Locale2".
Frasi brevi ma legate, non frammenti slegati. 🤘 come firma se ci sta bene nel punto
giusto, non forzata.

## Prima di consegnare

- Controlla zero em-dash, zero bullet point.
- Controlla che ogni band citata sia davvero programmata quella settimana secondo
  l'elenco fornito (non aggiungere/dimenticare band per errore di trascrizione).
- Se hai dovuto usare placeholder per handle non verificati, elencali chiaramente a
  parte insieme alla caption, non nasconderli in mezzo al testo.

Il carosello grafico che accompagna questa caption lo prepara Vale a mano — questa
skill produce solo il testo. Per caricare e programmare il post una volta pronto,
passa alla skill `meta-schedule`.

## Vedi anche

- [[Calendario-Editoriale]] — perché è un roundup di tutte le band, non mono-band
- [[Tone-of-Voice]] — zero em-dash, zero bullet point, tono narrativo
- `meta-schedule` — per caricare e programmare il post una volta scritta la caption
