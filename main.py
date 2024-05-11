from config import *

# remplazar por la direcion ingresado
ruta = '/home/william/Escritorio/Base-de-datos-de-documentos/archivos' 
archivos = laod_file(ruta)

print ("Generacion de una base de datos de documentos")
texto=input("Busqueda: ")
sheatch_text(texto,archivos)

