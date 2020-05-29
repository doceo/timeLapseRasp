import os
import time
from ftplib import FTP


ftp = FTP('192.168.1.182')   # Si connette all'host sulla porta predefinita
ftp.login('testFTP', 'testrasp01')  # utente anonymous, password anonymous@
ftp.retrlines('LIST')     # elenca il contenuto della directory

percorso = "/Public/timelapse/"

print (ftp.pwd())

ftp.retrlines('LIST')     # elenca il contenuto della directory

immagini = os.listdir('image')

giorno = immagini[0]
cartella = giorno[:15]

print(cartella)


print (percorso)
print(os.getcwd())
ftp.cwd(percorso)
ftp.mkd(cartella)

i = 0

while i < len(immagini):
#	print(immagini[i])
	i = i + 1

ftp.quit()
