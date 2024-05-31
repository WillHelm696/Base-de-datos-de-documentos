from config import *
from prueba2 import *
import argparse
import sys
#from limpieza import *

def create_bd(ruta):
    #busca la dirrecon de los archivos
    archivos = load_file(ruta)
    new_bd(archivos)

def shearch_text(texto):   
    print("Busqueda")
    new_search(texto)

def operaciones(args):
    if args.operation == 'create':
        create_bd(args.argumento)
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
