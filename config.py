from TF_IDF import *
from triee import *
import os
import PyPDF2
from prueba2 import *

# Guarda en una lista las rutas de los archivos 
def load_file(ruta):
    lista = os.listdir(ruta)
    archivos = []
    for item in lista :
        contenido = os.path.join(ruta,item)
        if os.path.isfile(contenido):
            archivos.append(contenido)
        elif os.path.isdir(contenido):
            #Si hay una carpeta agrega los archivos de la carpeta a la lista
            archivos += load_file(contenido)
    return archivos

def leer_txt(item):
    with open(item,'r',encoding='utf-8') as archivo:
        text = archivo.read()
    return text

def leer_pdf(ruta):
    with open(ruta, 'rb') as archivo_pdf:  # Abre el archivo en modo binario ('rb')
        lector = PyPDF2.PdfReader(archivo_pdf)
        texto = ""
        for pagina in lector.pages:
            texto += pagina.extract_text()
    return texto

def bd_documents(lista):
    documents = []
    for item in lista:

        if item.endswith(".pdf"):
            text = leer_pdf(item)
            #token = tokenizacion(text)
        elif item.endswith(".txt"):
            text = leer_txt(item)
            #token = tokenizacion(text)
        #print(token)
        documents.append(text)         
    bd=Tf_Idf(documents)

    for index in bd:
        print('\n')
        print(bd[index])

def shearch_text(text,datos):
    print('\n')
    return
