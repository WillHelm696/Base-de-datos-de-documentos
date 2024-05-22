from config import *
from prueba2 import *
#from limpieza import *

# busca la dirrecon de los archivos
ruta=os.getcwd()
ruta = os.path.join(ruta,"archivos")
#ruta = os.path.join(ruta,"archivos\\prueba-lu")

#carga los archivos a aun arreglo sustituir por trie
archivos = load_file(ruta)

print ("Generacion de una base de datos de documentos")
#texto=input("Busqueda: ")
texto="hi"
token = tokenizacion(texto)
print("Tokens de texto:")
print(token)

#Creasion de Base de datos con los documentos
bd_document=bd_documents(archivos)

#shearch_text(token,bd_document)

#print(clean_text(archivos[0]))

#nuevo_trie=convert_to_trie(archivos)
#print(nuevo_trie.root.key)
#print(get_all_words(nuevo_trie))
