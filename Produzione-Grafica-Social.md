---
tags: [kb, grafica, produzione, social, tecnico, MARKETING]
aggiornato: 2026-08-17
---

# Produzione Grafica Social

← [[_CLAUDE-TRIBUTE-NATION|Indice]]

> Specifiche tecniche di produzione per carosello Instagram, slide Spotlight e story (1080x1080 / 1080x1920). Integrato dal briefing di passaggio del 2026-08-16. Vedi [[Identita-Visiva]] per palette/font a livello di brand e [[Regole-Operative-Claude]] per gli errori noti da non ripetere.

## Sfondo standard

Sfondo `#0A0A0A` con glow rosso radiale al centro (GaussianBlur 100px, intensità verso i bordi).

## Struttura slide carosello (1080x1080)

- Logo TN in basso centrato (190-200px width), semitrasparente
- @_tribute_nation_ e numero slide nel footer
- Pad laterale: 90px
- Linee divisorie: `#2A2A2A`, 1px
- Tag rubrica rosso `#CC2200`, DM Sans 18pt — 🔧 in produzione Pillow (px, non pt Canva) questo valore risultava troppo piccolo: usare almeno 26px, verificato sul pacchetto di prova Frøm Zerø (2026-08-16) dopo feedback diretto di Vale ("i testi sono troppo piccoli, soprattutto i più piccoli")
- Titolo principale Bebas Neue bianco 64-96pt
- Corpo testo DM Sans grigio `#AAAAAA` 22-26pt — stesso caveat sopra: in Pillow serve almeno 33px per essere leggibile (valore finale dopo due giri di ingrandimento, 2026-08-16)
- Handle footer `@_tribute_nation_`: almeno 22px (non documentato prima, causava testo footer illeggibile)
- CTA in rosso `#CC2200`
- Centramento verticale: usare misurazione reale word-wrap per centrare nell'area disponibile (`AREA_TOP=60`, `AREA_BOT=H-110`)

## Slide cover Spotlight

- Foto live come sfondo
- Grade: scurimento 0.6-0.65, boost rosso x1.4-1.5, taglio blu x0.5-0.55 — su foto con dominante calda/verde (luce diurna, palchi esterni) serve anche tagliare il verde (x0.55 circa) per evitare una dominante olivastra invece che rossa: verificato sul pacchetto Frøm Zerø (2026-08-16)
- Vignetta vettoriale x0.9 (NON loop pixel, usare numpy broadcasting)
- **Logo band + nome banda sotto** (deciso da Vale il 2026-08-16, sostituisce "nessun testo aggiuntivo": ora il nome banda va scritto sotto il logo, Bebas Neue bianco ~72px). Stesso ingombro verticale complessivo di prima (il vecchio standard "solo logo 700px" era comunque impreciso — misurato sul pixel reale del pacchetto Wonderwall risultava ~480px): logo ridotto a **~390px** + gap ~22px + nome banda, così la somma resta vicina ai ~480px di prima e la foto sotto non viene coperta più di quanto lo fosse già
- Blocco logo+nome centrato orizzontalmente, **centro verticale al 72% dell'altezza del canvas** (non a metà) — lascia visibile la parte superiore della foto (viso/busto del performer) sopra il badge

## Slide contenuto Spotlight

- Logo band 280-300px in alto
- Tag rubrica rosso, divisore, testo centrato
- **Titolo sempre bianco** (Bebas Neue, ~70px se corto/una riga, ~58px se più lungo/due righe — valori finali del 2026-08-16, dopo due giri di ingrandimento su richiesta di Vale). 🔧 **Decisione ribaltata il 2026-08-16**: durante la prova Wonderwall era emerso un titolo rosso per statement/numeri a effetto (es. "ANNI '90."); Vale ha chiesto di tornare a **tutti i titoli bianchi**, anche per le slide-statement — leggibilità migliore a schermo. Non usare più il rosso per i titoli in nessun caso, incluso il pull-quote di chiusura (vedi sotto).
- Corpo testo: **33px** (valore finale, dopo due ingrandimenti da un 25px iniziale troppo piccolo)
- Footer: solo logo TN + handle `@_tribute_nation_`, **senza numero di slide esplicito** (verificato sul pacchetto Wonderwall) — 🔧 la voce "numero slide nel footer" più sotto era nella KB prima di questa verifica diretta: confermare con Vale se altri spotlight già pubblicati lo includono davvero o se va corretta anche lì
- Sequenza di tag rubrica tipica su un arco di 9 slide (esempio Wonderwall): CHI SONO → PERCHÉ [ARTISTA ORIGINALE] → L'EPOCA D'ORO → IL LIVE → UN ANEDDOTO → FUORI DAL PALCO → IMITARE O TRASMETTERE → IL CONSIGLIO (chiusura)
- **TRIBUTE TO TRIBUTE** (dal 2026-08-16, sostituisce il vecchio nome italiano "Band rispettate"): tag in inglese, unico tag non in italiano nella sequenza standard, per la slide/citazione quando la band nomina una tribute italiana che stima — solo se la domanda 8 del questionario dà una risposta citabile (vedi [[Pipeline-Contenuti-e-Roster]]), non è fissa in ogni spotlight

## Slide di chiusura (ultima del carosello)

- Stessa struttura delle slide contenuto (tag "IL CONSIGLIO" o simile) ma con pull-quote/citazione della band come titolo — **titolo bianco come tutte le altre slide** dal 2026-08-16 (prima era rosso, vedi sopra), ~62px se corto/una riga, ~50px se più lungo
- CTA testuale ("Seguili su Instagram") in bianco/grigio chiaro, **non** rosso — la nota "CTA in rosso" nelle specifiche generali sopra si riferisce ad altri contesti (story, non questa slide)

## Format storia (1080x1920)

- Safe zone: 160px top/bottom
- Logo TN in fondo (`H-lh-30`)

## Regola fondamentale grafica

Meno testo possibile. La grafica crea curiosità, la caption racconta la storia. Non scrivere tutto: lasciare in sospeso.

## Note tecniche produzione (Python/Pillow)

```python
# Font (scaricare se non presenti)
BEBAS = "/tmp/fonts/BebasNeue.ttf"
DM_SANS = "/tmp/fonts/DMSans.ttf"
# wget da github.com/google/fonts

# Colori
BG = (10, 10, 10)
RED = (204, 34, 0)
WHITE = (255, 255, 255)
GREY = (185, 185, 185)
DARK_GREY = (42, 42, 42)
FOOT_GREY = (70, 70, 70)

# Logo TN: rimuovere pixel neri (trasparenza)
data[(r<40)&(g<40)&(b<40), 3] = 0

# Vignetta vettoriale (numpy, NON loop pixel)
xs = np.arange(W)[np.newaxis,:]
ys = np.arange(H)[:,np.newaxis]
dist = np.sqrt((xs-cx)**2 + (ys-cy)**2) / (np.sqrt(2)*cx)
vign = np.clip(1 - dist*factor, 0, 1)[:,:,np.newaxis]
arr = np.clip(arr * vign, 0, 255)

# Centramento verticale reale
# misurare altezza con draw_c_measure (word wrap reale)
# poi: y_start = AREA_TOP + max(0, (AREA_BOT-AREA_TOP-total)//2)

# PDF: strip emoji (i font PDF non le supportano)
import re
emoji_pattern = re.compile(
    "[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F9FF\U0001FA00-\U0001FAFF"
    "\U00002702-\U000027B0\U000024C2-\U0001F251]+",
    flags=re.UNICODE)
clean = emoji_pattern.sub('', text)

# Emoji nelle grafiche: usare Twemoji PNG (non caratteri unicode)
# urllib.request.urlretrieve(
#   "https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/{code}.png",
#   path)
```

Altri errori noti da non ripetere (rendering Pillow) sono in [[Regole-Operative-Claude]] (emoji, accenti italiani, cirillico).

## Template PDF (Articolo e Caption)

Schema dedotto dai PDF reali del pacchetto Wonderwall e replicato per la prova Frøm Zerø (2026-08-16, generati con Python/reportlab):

- Sfondo pagina pieno `#0A0A0A`, logo TN orizzontale (`LOGO_ORIZZONTALE_RED.png`) in alto a sinistra su ogni pagina
- Titolo Bebas Neue bianco, poi linea divisoria sottile grigia, poi corpo DM Sans grigio chiaro
- Ogni H2 preceduto da una linea divisoria
- **Citazioni dirette in box con bordo rosso `#CC2200`** (spessore ~1-1.5pt, padding interno, testo bianco) — questo è il modo concreto in cui si applica la regola "blockquote" di [[Tone-of-Voice]] nei PDF
- Footer identico su ogni pagina: `@_tribute_nation_ · www.tributenation.it` in basso a sinistra (grigio scuro), numero pagina in basso a destra
- Caption PDF: titolo `{BAND} — CAPTION SPOTLIGHT`, stessa struttura, hashtag in rosso, **emoji sempre rimosse** (coerente con la regola già nota)

## Struttura pacchetto Spotlight

Ogni spotlight produce questo set di file (nomi verificati sul pacchetto Wonderwall, 2026-08-16 — correggono una versione precedente di questa nota):

- `{Band}_Articolo.md` — articolo Markdown (nome banda capitalizzato)
- `{Band}_Articolo_WordPress.html` — HTML per CMS
- `{Band}_Articolo.pdf` — PDF branded
- `{Band}_Caption.md` — caption con emoji per IG
- `{Band}_Caption.pdf` — PDF senza emoji
- `{Band}_Logo.png` — logo con canale alpha (sfondo trasparente, badge logo opaco al centro; non necessariamente col suffisso "_smascherato")
- `{band}_slideN_tema.png` — 9 slide carosello 1080x1080, nome banda minuscolo, N senza zero iniziale, suffisso descrittivo del contenuto (es. `wonderwall_slide1_cover.png`, `wonderwall_slide4_epoca.png`) — stesso schema già documentato in [[Materiali-NAS]] (regola 6)
- `{Band}_Pacchetto.zip` — tutto compresso

Emoji sempre rimosse dai PDF (font non le supportano), presenti invece nel `.md` per la pubblicazione IG.

## Formato "statement card" (Spoiler Spotlight, B-Side, Dalla Nation per la Nation)

Diverso dal carosello Spotlight a 9 slide: qui ogni slide è un blocco di testo centrato (nessun logo band), stesso sistema visivo (sfondo/font/colori/footer). Script dedicato `tools/spotlight/make_statement_slides.py` (riusa le funzioni di `make_slides.py`: sfondo, wrap, footer, font), config JSON per slide con lista di blocchi testo (font bebas/dmsans, size, colore, divider opzionale dopo). Supporta anche una progress bar in basso per i caroselli multi-slide (`progress_total`/`progress_index` nel config), come nel formato "Dalla Nation per la Nation".

- **Spoiler Spotlight**: slide singola, cita solo la band **originale** (mai la tribute, vedi [[Tone-of-Voice]]), tipicamente due elementi identificativi (anno/luogo/titolo disco) più riga di chiusura "Domani lo Spotlight."
- **B-Side**: slide singola, segue la formula in [[Calendario-Editoriale]] (dato inaspettato → pivot → chiusura verso la tribute italiana, riga finale rossa)
- **Dalla Nation per la Nation**: carosello 5 slide con progress bar, salvato in `DALLA NATION PER LA NATION\<D_MM_YY>\` (solo cartella con PNG, niente zip duplicato — regola 4 di [[Materiali-NAS]])
- **Nation Garage** (formato deciso il 2026-08-26, prima 🔧 da confermare): carosello a N slide con progress bar, stesso motore statement-card, un tool/argomento per slide, salvato in `NATION GARAGE\<D_MM_YY>\`

Verificato il 2026-08-17 sul pacchetto Desaparecidos (spoiler) / Soundgarden-Outshined (b-side) / community question (dalla nation, 21/08). 🔧 Attenzione accenti italiani nei config JSON: scrivere sempre il carattere accentato reale (è, à...) — un giro di prova aveva usato "e'" come placeholder ASCII per evitare problemi di encoding, non necessario: il font li supporta nativamente, va solo scritto il JSON con Write/Edit (non heredoc bash).

## Vedi anche

- [[Identita-Visiva]] — palette e font a livello di brand
- [[Regole-Operative-Claude]] — errori noti di rendering
- [[Pipeline-Contenuti-e-Roster]] — processo spotlight che genera questo pacchetto
