---
tags: [kb, sito, funzionalita, area-riservata, MARKETING, WEB]
aggiornato: 2026-09-06
---

# Funzionalità Sito e Area Riservata

← [[_CLAUDE-TRIBUTE-NATION|Indice]]

> Vedi [[Identita-e-Ruolo]] per i ruoli dei due co-fondatori. Cronologia in [[LOG]].

## Cosa offriamo oggi ai clienti

### Vetrina pubblica

Ogni tribute band ha una scheda pubblica completa: bio, formazione, foto, video, contatti, e una sezione "prossimi live" che si aggiorna da sola (nessun lavoro manuale). Il sito espone un calendario eventi pubblico con ricerca per tutta la scena, oltre a un blog editoriale con gli Spotlight.

**Mappa della Nation** (`/mappa-live-band/`, verificata live il 2026-08-26): mappa d'Italia interattiva con due viste alternabili, "Copertura band della Nation" e "Dove sono i live", filtro per regione/provincia e lista laterale collegata ai pin sulla mappa. Al 2026-08-26 mostra 51 band in 19 province (contro le 47 band con pagina sito registrate il 2026-08-16 — il roster pubblicato è cresciuto nel frattempo, numero da rivedere periodicamente, non fissare).

### Accesso gratuito per le band ("Entra nella Nation")

Le band possono candidarsi gratuitamente per una pagina sul sito, candidarsi per uno Spotlight, e compilare un form rapido per aggiungere una sola data — tutto senza bisogno di account. I form sono protetti da invii doppi accidentali.

### Accesso gratuito per i locali ("Entra nella Nation Venue")

Stesso principio: candidatura gratuita per la scheda locale (con controllo automatico dei duplicati) e form per segnalare più serate contemporaneamente, con possibilità di includere una locandina.

**Gestione autonoma della scheda locale (confermata attiva, 2026-09-06)**: con un account gratuito, un locale rivendica la propria scheda e la gestisce in autonomia dall'area riservata, esattamente come le tribute band — stesso meccanismo descritto sopra per l'Area riservata band. Corregge la nota precedente che la dava come "sviluppata, non ancora attiva".

### Area riservata (novità di agosto)

Chi gestisce una band può registrarsi, fare login e "rivendicare" la propria band nel roster (con approvazione di Daniele/Nobody), dopodiché può:

- Inserire le proprie date in autonomia
- Modificare la propria scheda pubblica (testi, foto, fino a 20 foto in galleria), online subito senza approvazione
- Per i dati delicati (nome, città, genere), utilizzare un pulsante "Richiedi una modifica" che passa comunque a Daniele

Una band può avere più gestori con accessi indipendenti.

### Bot Telegram "Date per Città"

Chiunque scrive "che date ci sono a Milano?" e riceve i prossimi live in quella città, con link cliccabili. È utile ai fan e offre visibilità gratuita per band e locali.

## Il Monitor: cruscotto interno di Daniele

Da inizio agosto esiste una pagina di amministrazione riservata a Daniele, pensata per avere tutto il progetto sotto controllo da un unico posto. Non è visibile ai clienti: è puro lavoro interno.

**A cosa serve:**

- Numeri a colpo d'occhio: richieste in attesa di approvazione, band gestite, iscritti, account non verificati, account sospesi
- Vista su ogni band: chi la gestisce, se ha uno Spotlight pubblicato o in programma, se manca ancora un gestore o un contatto email — permette di vedere subito quante band sono ancora "orfane" senza nessuno che le segua
- Tutto ciò che succede sul sito lato utenti: richieste di rivendicazione, nuove registrazioni, accessi riusciti/falliti, segnalazioni di sicurezza, chi ha caricato foto/locandine, messaggi scambiati con le band
- Ricerca unica che cerca contemporaneamente in tutte queste categorie
- Filtri, ricerca ed esportazione dei dati per ogni sezione

**Rilevanza oltre il tecnico:**

Il Monitor è lo strumento con cui Daniele risponde rapidamente a domande come "quante band non hanno ancora un gestore?", "chi si è appena registrato?", "quali richieste sono ferme da giorni?" — utile per capire dove concentrare outreach e follow-up editoriale, dato che non esiste ancora un analytics del sito.

Il Monitor è cresciuto per versioni successive (l'ultima, "v6", è dell'11/08/2026) ed è esclusivamente di sola lettura più qualche azione puntuale già esistente altrove (approvare/rifiutare una richiesta, rimuovere un gestore): non è un pannello con cui si "cambiano le cose", ma un pannello con cui si vedono le cose.

## Funzionalità già sviluppate ma non ancora attive

- **Dati per Google** (SEO) sulle schede band: pronti, non ancora pubblicati
- **Filtri di ricerca su band** (nome, artista tributato, genere): questi sono già attivi dall'8/08

### Directory pubblica dei locali

L'Area Venue del sito è online — dettaglio completo, numeri e cronologia in [[Venue-Tracker]].

## Area Fan con account (confermata attiva, 2026-09-06)

Corregge la nota precedente ("i fan hanno solo form di contatto e il bot Telegram, nessun account personale"): i fan hanno oggi un account gratuito vero (email o login social Google/Facebook), possono seguire le band preferite, ricevere notifiche su nuove date su tre canali (push, email, Telegram), generare un link calendario che si aggiorna da solo, commentare sotto schede e articoli, installare il sito come PWA, e cancellare account/dati in autonomia. Dettaglio completo: [[16 - Post Funzionalità Fan]].

## Cosa NON è ancora disponibile

Attenzione: non comunicare i seguenti come funzionalità già attive:

- **Analytics del sito** (GA4): non è ancora acceso — nessun numero reale di traffico disponibile da mostrare a una band come prova di valore
- **Email diretto sulla scheda band**: nessun campo email pubblico sulla pagina del sito (solo via Notion/casella email principale) — quindi nessun avviso automatico "una band a cui interessa" è possibile oggi
- **Il Monitor come servizio clienti**: non è una funzionalità del sito per band/locali/fan — è uno strumento interno di Daniele. Non va mai citato in comunicazioni verso clienti.

## Vedi anche

- [[Identita-e-Ruolo]]
- [[Stack-Tecnico-Sito]]
- [[Stato-e-Roadmap]]
- [[Venue-Tracker]]
