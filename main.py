from config import *
from prueba2 import *
import argparse
import sys
#from limpieza import *

def create_bd(ruta):
#busca la dirrecon de los archivos

#ruta=os.getcwd()
#ruta = os.path.join(ruta,"archivos")
#ruta = os.path.join(ruta,"archivos\\prueba-lu")

#carga los archivos a aun arreglo sustituir por trie
    print("Base de datos")
    archivos = load_file(ruta)
    bd_document=bd_documents(archivos)
    print(bd_document)

def shearch_text(texto):   
    print("Busqueda")
    token = tokenizacion(texto)
    print("Tokens de texto:")
    print(token)

#nuevo_trie=convert_to_trie(archivos)
#print(nuevo_trie.root.key)
#print(get_all_words(nuevo_trie))

def operaciones(args):
    if args.operation == 'create':
        create_bd(args.argumento)
        print("crear base de datos")
    if args.operation == 'search':
        shearch_text(args.argumento)

def main():
    parser = argparse.ArgumentParser(description='Crear o buscar en la base de datos.')
    parser.add_argument('operation', choices=['create', 'search'], help='Operación a realizar: create | search')
    parser.add_argument('argumento', help='Ruta a la carpeta de documentos o texto a buscar')

    args = parser.parse_args()
    operaciones(args)

if __name__ == '__main__':
    main()