from config import *

# busca la dirrecon de los archivos
ruta=os.getcwd()
ruta = os.path.join(ruta,"archivos")

#carga los archivos a aun arreglo sustituir por trie
archivos = load_file(ruta)

print ("Generacion de una base de datos de documentos")
texto=input("Busqueda: ")

token = tokenizacion(texto)
print("Tokens de texto:")
print(token)

#Creasion de Base de datos con los documentos
bd_document=bd_documents(archivos)

shearch_text(token,bd_document)
