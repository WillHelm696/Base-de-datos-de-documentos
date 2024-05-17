import os
import PyPDF2
import re

# Guarda en una lista las rutas de los archivos 
def laod_file(ruta):
    lista = os.listdir(ruta)
    archivos = []
    for item in lista :
        contenido = os.path.join(ruta,item)
        if os.path.isfile(contenido):
            archivos.append(contenido)
        elif os.path.isdir(contenido):
            #Si hay una carpeta agrega los archivos de la carpeta a la lista
            archivos += laod_file(contenido)
    return archivos

def leer_txt(item):
    with open(item,'r') as archivo:
        text = archivo.read()
    return text
import PyPDF2

def leer_pdf(ruta):
    with open(ruta, 'rb') as archivo_pdf:  # Abre el archivo en modo binario ('rb')
        lector = PyPDF2.PdfReader(archivo_pdf)
        texto = ""
        for pagina in lector.pages:
            texto += pagina.extract_text()
    return texto

def sheatch_text(text,lista):
    for item in lista:
        print("-------------------------------------------------------------------------------------------------------")        
        print(item)
        print('\n')
        if item.endswith(".pdf"):
            text = leer_pdf(item)
            token = tokenizacion(text)
            #################################
            """
            lineas = text.split('\n')
            for linea in lineas:
                print(linea)
            """
            #################################
        elif item.endswith(".txt"):
            text = leer_txt(item)
            token = tokenizacion(text)
            #################################
            """
            cont=0
            for linea in text:
                if text in linea:
                    
                    cont+=1
                    print(linea.index(text))
                    print(linea.strip())

            if cont == 0:
                print("document not found")
            """
        #################################
        
        print(token)

def tokenizacion(texto):
    # Dividir el texto en tokens utilizando expresiones regulares
    tokens = re.findall(r'\b\w+\b', texto)
    return tokens

"""
import spacy

# Cargar el modelo de lenguaje
nlp = spacy.load('es_core_news_sm')

def tokenizacion_nlp(texto):
    # Procesar el texto con SpaCy
    doc = nlp(texto)
    # Extraer tokens
    tokens = [token.text for token in doc]
    return tokens


#texto=texto.lower()
#texto=texto.split(' ')
"""

