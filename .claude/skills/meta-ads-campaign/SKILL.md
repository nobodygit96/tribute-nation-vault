---
name: meta-ads-campaign
description: >
  Costruisce e pubblica una campagna pubblicitaria vera su Gestione Inserzioni
  Meta (adsmanager.facebook.com) — campagna, gruppo di inserzioni, inserzione
  con creatività, testi, destinazione e CTA. Usa quando l'utente chiede di
  "fare una sponsorizzata", "impostare una campagna Meta Ads" o "boostare un
  post" con budget vero. NON è la stessa cosa di programmare un post organico
  (per quello vedi meta-schedule) — qui si spende denaro reale, quindi ogni
  checkpoint di conferma con l'utente è obbligatorio, non opzionale. Usa ANCHE
  quando un'inserzione già impostata risulta bloccata da un errore misterioso
  tipo "campo link obbligatorio" con molti posizionamenti in rosso: è quasi
  sempre lo stesso problema noto, non un bug nuovo.
---

# Campagna pubblicitaria vera — Gestione Inserzioni Meta

Nato dal primo impianto reale di una campagna di recruiting band (2026-09-05):
un solo tentativo ha richiesto due inserzioni (la prima cancellata e rifatta)
prima di capire il vero blocco. Questa skill esiste per non ripetere lo stesso
giro di prova-errore la prossima volta.

**Principio guida**: qui si spendono soldi veri. Ogni azione irreversibile
(pubblicare, eliminare una bozza) richiede conferma esplicita dell'utente
*prima* di essere eseguita, non dopo. Se un'azione rischiosa è già partita per
errore, fermati e verifica subito lo stato reale (importo speso, stato
pubblicazione) invece di continuare come se niente fosse.

## Prima di iniziare

Verifica di avere già, confermati dall'utente:
- Obiettivo campagna, budget e durata.
- Targeting (interessi, età, geografia).
- Le creatività finite (immagini/video, tutti i formati necessari: feed
  quadrato + storia verticale, minimo) copiate nello scratchpad della sessione
  (non un percorso `Z:\` grezzo — `file_upload` accetta solo file leggibili
  dalla sessione).
- Testo primario, titolo, descrizione già scritti e approvati.
- L'account pubblicitario giusto: **solo** quello canonico con pagamento
  collegato (vedi [[Team-Marketing-AI-e-Meta-Ads]] per l'ID corrente) — mai il
  pulsante nativo "Metti in evidenza"/"Promuovi" di Instagram/Facebook, che
  porta a un account diverso senza il pagamento collegato.

## Passo 1 — Struttura: campagna → gruppo → inserzione

Crea (o riusa) nell'ordine. Se un'inserzione va rifatta da zero (vedi Passo 5),
**riusa il gruppo di inserzioni esistente** invece di ricrearlo: nel dialog
"Crea nuova campagna/inserzione" scegli "Usa un gruppo di inserzioni
esistente" — targeting e budget restano intatti, eviti di reimpostarli.

## Passo 2 — Caricare le creatività (serve Claude in Chrome, non basta il Browser pane)

Il Browser pane sandboxato non ha nessuno strumento di caricamento file. Serve
Claude in Chrome (`mcp__claude-in-chrome__*`, verifica con
`list_connected_browsers` che sia collegato). Tecnica (variante della stessa
usata in [[meta-schedule]], qui l'input va anche *appeso al DOM* perché
Gestione Inserzioni lo crea completamente scollegato):

1. Prima di cliccare "Carica", inietta l'hook:
   ```js
   window.__origClick = HTMLInputElement.prototype.click;
   HTMLInputElement.prototype.click = function() {
     if (this.type === 'file') { window.__capturedFileInput = this; return; }
     return window.__origClick.call(this);
   };
   ```
2. Clicca "Carica" nel selettore contenuti multimediali — l'input reale finisce
   in `window.__capturedFileInput`, senza aprire il dialog nativo.
3. **Appendi l'input al `document.body`** (a differenza del composer organico,
   qui l'input non basta renderlo visibile: va reso raggiungibile nell'albero
   DOM, altrimenti `find()` non lo troverà mai):
   ```js
   const inp = window.__capturedFileInput;
   inp.style.position = 'fixed'; inp.style.top = '0'; inp.style.left = '0';
   inp.style.zIndex = '999999';
   document.body.appendChild(inp);
   ```
4. `find("file input")` per il `ref`, poi `file_upload` con quel `ref` e il
   path assoluto di **un** file alla volta (carica singolarmente immagine feed
   e immagine storia, ripetendo l'hook per ognuna).
5. Rimuovi l'input e ripristina il prototype originale (`HTMLInputElement.prototype.click = window.__origClick; inp.remove();`)
   per pulizia, non è obbligatorio ma evita residui visivi.

## Passo 3 — Destinazione, URL, add-on: verifica sempre dopo un reload

Ogni volta che la pagina si ricarica (navigazione, riconnessione, sessione
persa) questi campi **tornano ai valori di default di Meta**, silenziosamente:
- "Destinazione" può tornare su "Evento di Facebook" invece di "Sito web".
- "Add-on del browser" può tornare su "App di messaggistica" (con
  Messenger/WhatsApp veri pre-collegati) invece di "Nessuno".

Prima di procedere oltre, **rileggi sempre questi due campi** con uno
screenshot o `javascript_exec` sui radio button, non fidarti che siano rimasti
come li avevi lasciati l'ultima volta che li hai guardati.

## Passo 4 — Il vero blocco: creatività per gruppo di posizionamento (non solo il selettore in alto)

Questo è il problema che causa l'errore **"Campo obbligatorio mancante: il
campo link è obbligatorio"** su 10+ posizionamenti contemporaneamente, e
**non è la Call to action** (vedi nota sotto — è una pista sbagliata su cui si
può perdere molto tempo).

Il vero motivo: quando crei un'inserzione, sotto "Creatività dell'inserzione"
Meta raggruppa i posizionamenti (es. "Feed, Inserzioni in-stream per i reel" /
"Stories, stato e Reels, Risultati della ricerca, App e siti") e assegna a
*ciascun gruppo* una creatività di **default auto-generata** (di solito il
logo della Pagina, 2000×2000, con testo placeholder tipo "Se ami le tribute
band, sei a casa 🎵...") — **indipendente** da quello che hai scelto nel
selettore "Contenuti multimediali" in cima alla sezione. Selezionare lì le tue
immagini reali (es. "2 di 10 selezionati") **non basta**: se non tocchi anche i
singoli gruppi, quei gruppi restano sulla creatività di default, e Meta blocca
la pubblicazione perché quella creatività di default non ha un link valido
agganciato.

**Correzione, per ogni gruppo elencato sotto "Creatività dell'inserzione":**
1. Espandi il gruppo (freccia a destra).
2. Clicca l'icona matita ("Modifica il gruppo").
3. Nel pannello che si apre, clicca "Cambia" sotto "Contenuto multimediale" e
   scegli l'immagine reale corretta per quel formato (quadrata per i gruppi
   feed, verticale 1080×1920 per i gruppi storie/reel).
4. Clicca su "Testo principale" e "Titolo" in quello stesso pannello: se
   mostrano ancora il testo di default auto-generato, sovrascrivilo con
   `ctrl+a` + digitazione del testo vero.
5. Salva quel gruppo, poi ripeti per ogni altro gruppo elencato.

Dopo aver corretto tutti i gruppi, il contatore avvisi in alto dovrebbe
scendere da "11 posizionamenti" a **massimo 1** (il posizionamento "Video con
premio di Audience Network" resta bloccato per chi non ha una creativa video —
è previsto, si ignora, non è un errore da risolvere).

### Nota sulla Call to action ("Vedi dettagli")

Il valore di default del menu "Call to action" è **"Vedi dettagli"** — è una
CTA reale e funzionante (si vede correttamente renderizzata nell'anteprima del
gruppo, pulsante cliccabile con link), **non un segnaposto vuoto**. Se serve
cambiarla (es. in "Iscriviti", l'opzione più vicina a "Registrati" — quella
label esatta non esiste tra le opzioni Meta) il menu a tendina è un widget
particolarmente ostile all'automazione: click diretti, doppio click, invio e
barra spaziatrice da tastiera falliscono silenziosamente nella maggior parte
dei tentativi. Se serve cambiarla, prova prima a farlo scrivere direttamente
all'utente nel browser (un solo click, banale per un umano); se devi
insistere in automazione, l'unica sequenza che ha funzionato una volta è:
aprire il menu, scrivere il tasto iniziale dell'opzione voluta per il
type-ahead (es. "i" per "Iscriviti", che la evidenzia con bordo di focus), poi
cliccare con precisione al centro della riga ormai pienamente visibile (non
tagliata dal bordo della lista) — ma non è affidabile al 100%, e comunque
**non è mai bloccante**: se il tempo stringe, lascia "Vedi dettagli".

## Passo 5 — Se un'inserzione resta bloccata e non si risolve

A volte è più veloce eliminare l'inserzione (bottone "Elimina la bozza", con
conferma) e ricrearla da zero **nello stesso gruppo di inserzioni** (Passo 1)
piuttosto che continuare a rincorrere lo stato guasto di quella singola bozza —
è quello che ha funzionato per rompere il problema del Passo 4 la prima volta
che è successo. Chiedi sempre conferma esplicita all'utente prima di
eliminare, anche se si tratta solo di una bozza.

## Passo 6 — Verifica finale prima di pubblicare

Prima di cliccare "Pubblica":
1. Controlla il contatore avvisi (icona triangolo in alto nel pannello
   anteprima) — deve essere a 0, o al massimo 1 se l'unico residuo è il
   posizionamento video Audience Network.
2. Mostra all'utente un riepilogo di cosa sta per partire (creatività, testo,
   budget, durata, targeting) e aspetta conferma esplicita.
3. Solo dopo conferma, clicca "Pubblica". Meta stesso rifiuta la pubblicazione
   con un errore chiaro ("elementi non pubblicati perché presentavano errori")
   se qualcosa non va — non parte spesa né consegna finché non è tutto
   corretto, quindi un tentativo di pubblicazione con qualche dubbio residuo
   non è pericoloso in sé, ma **non sostituisce mai** la conferma esplicita
   dell'utente al punto 2.

## Passo 7 — Dopo la pubblicazione

Lo stato passa da "In bozza" a **"In fase di elaborazione"** (revisione Meta,
da pochi minuti a 24h) — non "Attivo": nessuna spesa parte finché la revisione
non approva. Verifica "Importo speso" = €0,00 subito dopo, e riporta
chiaramente all'utente che la campagna è ora in revisione, non ancora
live/spendente.

## Vedi anche

- [[Team-Marketing-AI-e-Meta-Ads]] — account pubblicitario corretto, storico
  decisioni budget/targeting per ogni campagna
- [[meta-schedule]] — programmazione organica (Business Suite), tecnica
  gemella per il caricamento file ma composer diverso
- [[Regole-Operative-Claude]] — regola di sicurezza sull'account pubblicitario
