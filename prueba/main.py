from search_word_in_file import *
archivo1='archivo1.txt'
archivo2='archivo2.txt'
archivo3='archivo3.txt'
archivo4='archivo4.txt'
archivos=[archivo1,archivo2,archivo3,archivo4]

print ("Generacion de una base de datos de documentos")
texto=input("Busqueda: ")

for file in archivos:
    sheatch_text(texto,file)
    print("------------------------------------------------------------------------------------")
