from config import *

# remplazar por la direcion ingresado
ruta2='/data/data/com.termux/files/home/storage/shared/FDI-LLC/Base-de-datos-de-documentos/archivos'
ruta = '/home/william/Escritorio/Base-de-datos-de-documentos/archivos' 
archivos = laod_file(ruta2)

print ("Generacion de una base de datos de documentos")
texto=input("Busqueda: ")
sheatch_text(texto,archivos)

token = tokenizacion(texto)
print("Tokens de texto:")
print(token)


# Ejemplo de texto
texto = "La tokenización es el proceso de dividir un texto en unidades más pequeñas."

# Aplicar tokenización
tokens = tokenizacion(texto)

# Imprimir tokens
print("Tokens:")
print(tokens)
