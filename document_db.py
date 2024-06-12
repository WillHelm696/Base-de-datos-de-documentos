from config import *
import argparse
import sys

def create_bd(ruta):
    # busca la dirrecon de los archivos
    archivos = load_file(ruta)
    create_db(archivos)

def search_text(texto):
    print("Busqueda")
    search(texto)

def operaciones(args):
    if args.create:
        create_bd(args.create)
    if args.search:
        search_text(args.search)

def main():
    parser = argparse.ArgumentParser(description='Crear o buscar en la base de datos.')
    # Añade los argumentos para create y search
    parser.add_argument('-create', help='Ruta a la carpeta de documentos entre comillas')
    parser.add_argument('-search', help='Texto a buscar')
    
    args = parser.parse_args()
    # Verifica qué operación se debe realizar
    operaciones(args)

if __name__ == '__main__':
    main()
