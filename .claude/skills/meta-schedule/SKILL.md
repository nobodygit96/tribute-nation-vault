---
name: meta-schedule
description: >
  Carica immagini/slide e caption su Meta Business Suite (business.facebook.com)
  e programma o pubblica il post su Facebook e Instagram, gestendo le insidie
  reali dell'interfaccia (input file nascosto, spinbutton di ora/minuti, upsell
  pubblicitario dopo il click). Usa quando l'utente chiede di "programmare",
  "schedulare" o "pubblicare" un post/contenuto su Meta/Facebook/Instagram, o
  dice "carica queste slide e programmale per <data>". Usa ANCHE quando qualcosa
  nel composer di Meta Business Suite si comporta in modo strano (data che non si
  aggiorna, toggle che sparisce, campo che sembra vuoto dopo aver scritto) — sono
  quasi sempre gli stessi 4-5 problemi noti, non un bug nuovo da investigare da zero.
---

# Programmazione post — Meta Business Suite

Nato da 5+ post programmati a mano nella stessa sessione (2026-09-01/03): è il compito più
ripetuto nella produzione settimanale di Tribute Nation, ed è anche il più fragile
dell'intero flusso — l'interfaccia di Meta non espone i controlli in modo standard,
quindi le tecniche sotto non sono opzionali, sono l'unico modo che funziona.

**Principio guida**: ogni passo qui esiste perché il modo "ovvio" di farlo ha fallito
almeno una volta in sessione reale. Seguili nell'ordine, non improvvisare scorciatoie —
soprattutto sui campi data/ora, dove un click imprevisto può disattivare un toggle o
lasciare un campo con la data sbagliata senza nessun errore visibile.

## Prima di iniziare

Verifica di avere già pronti, in una cartella accessibile alla sessione (lo scratchpad,
non un percorso `Z:\` grezzo — copiaci prima i file se servono dal NAS):
- Le immagini/slide da caricare, nell'ordine in cui devono comparire nel carosello.
- Il testo della caption, già rivisto e approvato dall'utente (questa skill non scrive
  copy, lo pubblica).
- La data e l'ora di destinazione (o "adesso" se va pubblicato subito, non programmato).

## Passo 1 — Aprire il composer

Naviga a `https://business.facebook.com/latest/composer/?asset_id=<ASSET_ID>&business_id=<BUSINESS_ID>`
(gli ID sono quelli della Pagina/BM di Tribute Nation, chiedili se non li hai già in
sessione). Un composer fresco parte con "Pubblica su" TributeNation + @_tribute_nation_
già selezionati — non serve toccare quel campo.

## Passo 2 — Caricare le immagini (tecnica del file input nascosto)

Meta crea l'`<input type="file">` via JavaScript ma **non lo appende mai al DOM** —
`read_page`/`find` non lo trovano mai, e cliccare il bottone "Aggiungi foto/video" apre
un dialog nativo del sistema operativo che il browser automatizzato non vede. La tecnica
che funziona sempre:

1. Prima di cliccare il bottone, inietta questo hook via `javascript_tool`:
   ```js
   const origClick = HTMLInputElement.prototype.click;
   HTMLInputElement.prototype.click = function() {
     if (this.type === 'file') { window.__capturedFileInput = this; return; }
     return origClick.call(this);
   };
   ```
2. Clicca "Aggiungi foto/video" — il click viene intercettato, l'input reale finisce in
   `window.__capturedFileInput`, nessun dialog nativo si apre.
3. Rendi l'input visibile e utilizzabile da `find()`, via `javascript_tool`:
   ```js
   const el = window.__capturedFileInput;
   el.style.position = 'fixed'; el.style.top = '0'; el.style.left = '0';
   el.style.zIndex = '99999'; el.style.opacity = '1';
   el.style.width = '50px'; el.style.height = '50px';
   document.body.appendChild(el);
   ```
4. Usa `find("file input")` per ottenere il `ref`, poi `file_upload` con quel `ref` e i
   path assoluti di tutte le immagini in una volta sola (Meta le mette in coda
   nell'ordine passato).
5. Aspetta 2-3 secondi e controlla con uno screenshot che tutte le miniature siano
   comparse nell'ordine giusto prima di procedere.

## Passo 3 — Inserire la caption

Clicca nel campo "Testo", scrivi la caption. Dopo aver scritto, **verifica sempre** con
`javascript_tool`:
```js
document.activeElement.innerText
```
invece di fidarti solo dello screenshot. L'estensione Claude in Chrome a volte si
disconnette a metà digitazione riportando un errore, ma il testo è quasi sempre arrivato
comunque per intero — ricontrolla prima di ridigitare da capo (rischi testo duplicato).

Se un hashtag digitato apre un menu di autocompletamento sovrapposto (es. `#nomehashtag`),
premi `Escape` prima di continuare, altrimenti il testo successivo può finire inserito nel
punto sbagliato invece che in coda.

## Passo 4 — Programmare data e ora (la parte più delicata)

1. Individua il toggle "Imposta data e ora" (sezione "Programma") e attivalo con un click
   preciso sul toggle stesso — **non cliccare vicino**, un click a fianco può centrare
   invece l'intestazione della sezione e non succede nulla di visibile, ma il toggle resta
   spento e te ne accorgi solo dopo, quando i campi data/ora non compaiono.
2. Compaiono due gruppi di campi, Facebook e Instagram, ciascuno con un campo data
   (placeholder `gg/mm/aaaa`) e due spinbutton `ore`/`minuti`.
3. **Data**: clicca nel campo, `ctrl+a` per selezionare tutto il contenuto, digita la
   nuova data in formato `g/m/aaaa` (es. `4/9/2026`). A volte si apre un mini-calendario a
   popup sotto il campo: se compare, **clicca sul giorno evidenziato** per confermare,
   non fidarti che il testo digitato basti da solo. Il campo Instagram in particolare a
   volte non si aggiorna al primo giro — dopo aver impostato entrambi, rileggi i valori
   reali (vedi Passo 5) e ripeti solo quello rimasto indietro, con lo stesso identico
   procedimento.
4. **Ora**: sono spinbutton (`role="spinbutton"`, `aria-valuenow`), non campi di testo
   liberi — **non digitare le cifre direttamente**, il risultato è imprevedibile (es.
   digitare "1" poi "4" per ottenere 14 a volte produce 4, non 14). Usa invece `find("ore")`
   e `find("minuti")` per i `ref`, clicca per mettere il focus, poi premi `ArrowUp`/`ArrowDown`
   il numero di volte necessario per raggiungere il valore target (calcola la distanza più
   breve tra le due direzioni, tenendo conto del giro dell'orologio: da 21 a 14 conviene
   scendere di 7, non salire di 17).
5. Dopo aver impostato tutto, **verifica sempre i valori reali** prima di procedere (Passo 5)
   — non fidarti di come "sembra" lo screenshot, i campi di Meta a volte mostrano un valore
   diverso da quello effettivamente memorizzato finché non perdono il focus.

## Passo 5 — Verificare prima di inviare

Con `javascript_tool`, leggi i valori effettivi invece di interpretare uno screenshot:
```js
const spins = Array.from(document.querySelectorAll('[role="spinbutton"]'));
const dates = Array.from(document.querySelectorAll('input[placeholder="gg/mm/aaaa"]'));
spins.map(s => `${s.getAttribute('aria-label')}=${s.getAttribute('aria-valuenow')}`).join(' | ')
  + ' || dates: ' + dates.map(d => d.value).join(' | ');
```
Conferma che Facebook e Instagram abbiano **la stessa** data e ora attesa prima di
cliccare il bottone finale (che si chiama "Programma" se il toggle data/ora è attivo,
"Pubblica" se è spento — controlla anche questo, è un altro modo per accorgersi se il
toggle si è disattivato per sbaglio).

## Passo 6 — Pubblicare/programmare e gestire l'upsell

Clicca "Programma" (o "Pubblica" per un post immediato). Dopo la conferma ("Il tuo post è
programmato"/"è stato pubblicato"), Meta mostra quasi sempre un modal per trasformare il
post in un'inserzione a pagamento ("Raggiungi un pubblico più ampio..."). **Clicca sempre
"Forse più tardi"** — non avviare mai una sponsorizzazione da qui, è un'azione che spende
soldi reali e richiede una decisione esplicita separata dell'utente (vedi [[Team-Marketing-AI-e-Meta-Ads]]
per come si imposta una campagna vera, quando è quello che serve).

## Verifica finale

Naviga (o torna) al calendario di pianificazione e conferma visivamente che il post
compaia nel giorno/ora giusti, con tutte le immagini nell'ordine corretto. Riporta
all'utente cosa è stato programmato e per quando.

## Vedi anche

- [[Calendario-Editoriale]] — cosa esce ogni giorno della settimana
- [[Produzione-Grafica-Social]] — standard grafici dei contenuti che carichi qui
- [[Team-Marketing-AI-e-Meta-Ads]] — account pubblicitario giusto, errori noti sul "Metti in evidenza" nativo
