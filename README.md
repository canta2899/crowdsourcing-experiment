# Secondo Progetto Social Computing

## Cosa fare

### Fase 1

- [ ] Generate un task (insieme di HIT) con i seguenti requisiti:
    - Ci devono essere un totale di sei HIT
    - Ogni HIT deve contenere tre elementi che corrispondono a tre edizioni dei libri di cui si vogliono raccogliere i giudizi. Più precisamente, all'interno di ogni HIT i tre elementi di cui si vogliono raccogliere giudizi devono essere tre edizioni di  libri diversi. Le diverse edizioni di uno stesso libro devono invece comparire in HIT diversi (ossia, non ci devono essere edizioni diverse di uno stesso libro nello stesso HIT). Cercate di definire l’ordine degli elementi all’interno di ogni HIT in modo da evitare quando possibile il bias (ad es.,evitare che un dato libro compaia sempre nella stessa posizione).
    - Ogni edizione di un libro viene identificata dai seguenti attributi, i quali vannotutti e 7 mostrati ai worker:
        1) Titolo
        2) Autore
        3) Numero di pagine
        4) Editore
        5) Prezzo
        6) Copertina (da salvare come URL dell'immagine)
        7) Anno di pubblicazione
- [ ] Modificate opportunamente il layout HTML di *Crowd_Frame* in modo che si adatti ai requisiti sopra descritti, ovvero consenta  di visualizzare gli attributi di ciascun libro nel corpo del task
- [ ] Ogni HIT deve inoltre contenere nella parte iniziale (ossia, prima che il worker sia chiamato ad esprimere i giudizi delle edizioni dei libri) un questionario con almeno 4domande per catturare i gusti letterari ed il background del worker, ad es.:
    - Qual'è il tuo genere letterario preferito?
        1) Fantascienza
        2) Saggi
        3) Thriller
        4) ...
    - Quanti libri leggi in un mese?
        1) 0-1
        2) 2-5
        3) 6-10
        4) 11+
    - ...
- [ ] Per ciascun elemento (edizione), il worker deve valutare le seguenti dimensioni,tutte obbligatorie (fate attenzione a scegliere  la scala di valutazione corretta!):
    - "Acquisteresti questo libro?" (Si/No)
    - "Il prezzo di sembra adeguato?" (Si/No)
    - "Indica quanto ti sembra adeguato" (Slider con valori da min a max, scegliete voi min e max)
    - "Che impressione hai di questa edizione?" (Giustificazione scritta, almeno 10 parole)
- [ ] In aggiunta a quelle indicate sopra, aggiungete altre 2 dimensioni a piacere,scegliendo una scala di valutazione adeguata
- [ ] Scrivete delle adeguate istruzioni generali e istruzioni di valutazione
- [ ] Aggiungete un controllo di qualità sul tempo minimo di esecuzione del task, che deve essere di X secondi (scegliete voi X)
- [ ] Dispiegate il task utilizzando i metodi descritti a lezione e dettagliati sulle slides

### Fase 2

- [ ] Fate svolgere il vostro task ai membri di **almeno** altri 2 gruppi al fine di raccogliere idati di tutti e sei gli HIT (ossia, ognuno dei 6 membri degli altri due gruppi deve fare uno dei 6 HIT)
- [ ] Scaricate i dati finali prodotti dai worker del vostro task
- [ ] Create un grafico contenente un istogramma che mostri le frequenze relative delle risposte ai questionari
- [ ] Descrivete brevemente le caratteristiche dei worker del vostro task in base alle risposte date al questionario
- [ ] Calcolate le seguenti misure per ciascuna edizione:
    - Grado medio di adeguatezza del prezzo
    - Edizione con il livello massimo di adeguatezza del prezzo
    - Edizione con il livello minimo di adeguatezza del prezzo
- [ ] Aggregate i dati calcolati al punto precedente e:
    - Calcolate il grado medio di adeguatezza del prezzo
    - Calcolate lo scarto quadratico medio (deviazione standard) del grado di adeguatezza del prezzo
    - Determinate quale libro ha il grado più alto di adeguatezza del prezzo
- [ ] Elencate le giustificazioni fornite dai worker e:
    - Calcolate la lunghezza media
    - Determinate la giustificazione più lunga
    - Determinate la giustificazione più corta
- [ ] Descrivete brevemente le considerazioni tratte dall’analisi dei dati prodotti dai worker,incluse le due dimensioni a piacere del punto 5

## Informazioni aggiuntive

- Potete usare servizi come Goodreads per trovare edizioni diverse dello stesso libro(ad es., [questo](https://www.goodreads.com/work/editions/153313-nineteen-eighty-four). Se possibile, cercate di utilizzare edizioni di pari lingua/nazione
- Per generare gli HIT potete aiutarvi con il notebook fornito a lezione
- Per generare la configurazione del task potete aiutarvi con il generatore o farla manualmente
- Ricordate che il controllo di qualità sul tempo minimo che il worker deve passare su ogni elemento di un HIT comprende anche i questionari
- Per semplicità è sufficiente far svolgere il task a 6 worker (ossia, due gruppi), ma siete liberi di coinvolgere ulteriori gruppi

## Come consegnare

1. I gruppi devono essere formati da tre persone (i gruppi più o meno numerosi verranno penalizzati)
2. La consegna del progetto avviene in due fasi
3. Per la scadenza della Fase 1 bisogna consegnare il codice sorgente, ovvero:
    - Relazione di 3 pagine (con anche i vostri nomi cognomi e numeri di matricola)
    - Configurazione del task dispiegato (incluso l’URL del task dispiegato)
    - Codice sorgente di *Crowd_Frame* (evidenziate le vostre modifiche nella relazione)
4. Per la scadenza della Fase 2 bisogna consegnare i dati raccolti, ovvero:
    - Relazione di 3 pagine (con anche i vostri nomi cognomi e numeri di matricola) che descrive tutto il lavoro svolto
    - Dati finali prodotti dai worker durante lo svolgimento del task
5. **Scadenza**
    - **Fase 1: Martedì 15 Gennaio 2020**
    - **Fase 2: Domenica 20 Gennaio 2020**
6. Consegnare via mail a entrambi i docenti (un unico messaggio per fase, indirizzato a entrambi):
    - mizzaro@uniud.it
    - michael.soprano@uniud.it
    - oggetto della mail nel formato [Progetto SocCom 2 - Fase X] cognome1_cognome2_cognome3
    - in allegato alla mail un unico file zippato che quando scompattato produce una singola cartella con nome cognome1_cognome2_cognome3_fase_x
7. Punteggio
    - 5 punti in trentesimi per i migliori 20%
    - 4 punti per i seguenti 20%
    - 3 punti per i seguenti 20%
    - 2 punti seguenti 20%
    - 1 punto per i seguenti 20%
    - 0 punti a discrezione dei docenti per progetti non adeguati o per chi non consegna
