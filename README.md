# timeLapseRasp
## Istruzioni 
Scopo del progetto è la realizzazione di filmati in timelapse attraverso l'uso di raspberry, 
per la ripresa di eventi molto lunghi, della durata di giorni.

## Strumenti
* Raspberry Zero
* PiCamera

## Organizzazione del lavoro

### fotografie
Lo script è in bash, ricava la data e l'ora per assoviarla al nome del file.
Il file è generato dall'esecuzione di raspistill e viene salvato nella cartella image.

Lo script viene eseguito in modo periodico attraverso CRONTAB.

### impostazione di CRONTAB

Per verificare in linux l'esistenza di contrab bisogns digitare:

crontab -l

per inserire un'attività invece:

crontab -e

Digitare "i" (insert) per editare il crontab, quindi inserire il proprio cronJob.
Per salvare il crontab si digiti ":wq" (write and quite)
Se non si vuole salvare invece si digiti ":q" (quite)

La sintassi è semplice ed in rete ci sono autervoli guide, la riga scelta per questo
progetto garantisce una fotografia ogni 5 minuti, dalle 4 alle 22 di ogni giorno.

*/5 4-22 * * * sh PATH_ASSOLUTO/image.sh 2>&1

### timelapse

Per generare un video a partire dalle fotografie si è scelto mencorder,
di cui è facile trovare materiale in rete.
Per eseguire questo programma è necessario avere una lista dei nomi dei file, 
per ottenerla bisogna generarla subito prima di lanciare mencoder.

Portandosi nella cartella delle immagini, eseguire il seguente comando, facile da 
interpretare:
esegue una lista degli elementi della cartella con estensione -jpg e li invia
come flusso verso un file di nome stills.txt

ls *.jpg > stills.txt

A questo punto è possibile eseguire mencoder, il cui utilizzo è spiegato in molte guide nel web.

mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=1920:1080 -o timelapse.avi -mf type=jpeg:fps=24 mf://@stills.txt

