from TF_IDF import *
from triee import *
import os
import PyPDF2
#from prueba2 import *

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

def clean_text(texto):
  # Pasar el texto a minúsculas
  texto = texto.lower()
  words_to_remove={'si', 'a', 'sí', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 'en', 'entre', 'hacia', 'hasta', 
                 'mediante', 'para', 'por', 'pro','según', 'sin', 'so', 'sobre', 'tras', 'versus','vía', 'la','las','el','los'
                 'él','ella','ellos','yo','nosotros','vosotros','ustedes','usted','tú','vos','ellas','este','estos','ésta','esta','éste','éstas','esa','eso','esas','esos',
                 'aquellos','aquella','aquello','aquellas','aquel','mío','mi','tuyo','tu','tus','su','sus','nuestro','nos','le','suyo','suyos','míos','mía','mías','vuestro',
                 'tuya','tuyo','tuyos','tuyas','nuestra', 'nuestros','nuestras','suya','suyas','vuestra','vuestras','vuestros','ésto','les','y','o',
                 'que','como','te','se','lo','le','les','nos','me','se','mi','tu','su','nuestro','vuestro','mío','tuyo','suyo','nuestro','vuestro','míos','tuyos','suyos',
                 'unos','unas','unos','otro','otra','otros','otras','otro','otra','otro','es','son','soy','eres','es','somos','sois','son','estoy','estás','está','estamos'
                 ,'un'}
    # Crear un patrón de expresión regular que coincida con las palabras a eliminar
  pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in words_to_remove) + r')\b', re.IGNORECASE)
  # Usar la función sub de re para reemplazar las palabras no deseadas con una cadena vacía
  cleaned_text = pattern.sub('', texto)
  # Reemplazar letras con tilde por la misma letra sin tilde
  cleaned_text = re.sub(r'[áÁ]', 'a', cleaned_text)
  cleaned_text = re.sub(r'[éÉ]', 'e', cleaned_text)
  cleaned_text = re.sub(r'[íÍ]', 'i', cleaned_text)
  cleaned_text = re.sub(r'[óÓ]', 'o', cleaned_text)
  cleaned_text = re.sub(r'[úÚ]', 'u', cleaned_text)
  # Eliminar símbolos y números usando una expresión regular
  cleaned_text = re.sub(r'[^a-zA-Z\s]', '', cleaned_text)
  # Eliminar espacios extra generados por las eliminaciones
  cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
  return cleaned_text

def eliminar_acentos(texto):
    # Diccionario de caracteres con y sin acentos
    acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'À': 'A', 'È': 'E', 'Ì': 'I', 'Ò': 'O', 'Ù': 'U',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'Ä': 'A', 'Ë': 'E', 'Ï': 'I', 'Ö': 'O', 'Ü': 'U',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
        'Â': 'A', 'Ê': 'E', 'Î': 'I', 'Ô': 'O', 'Û': 'U',
        'ã': 'a', 'õ': 'o', 'ñ': 'n', 'Ã': 'A', 'Õ': 'O', 'Ñ': 'N',
        'å': 'a', 'Å': 'A', 'ç': 'c', 'Ç': 'C'
    }
    
    # Crear la tabla de traducción
    tabla_traduccion = str.maketrans(acentos)
    
    # Convertir el texto a minúsculas y aplicar la traducción
    texto = texto.lower()
    texto_sin_acentos = texto.translate(tabla_traduccion)
    
    return texto_sin_acentos

def bd_documents(lista):
    documents = []
    for item in lista:

        if item.endswith(".pdf"):
            text = leer_pdf(item)
        elif item.endswith(".txt"):
            text = leer_txt(item)
        
        text = clean_text(text)
        documents.append(text)
    #Calcula para documento el tf-ydf de cada palabra y lo guardacomo tupla
    bd_tf_idf = Tf_Idf(documents)
    """
    #Base de datos del la direcion y el trie de cada archivo
    document_bd= {}
    for index, sentence in enumerate(bd_tf_idf):
        trie_doc = Trie()
        for tupla in sentence:
            #Inserta cada palabra y tf-idf en el triee
            insert(trie_doc,tupla)
        # Guarda como una tupla la direcion del archivo y el trie del archivo
        document_bd[index]=(trie_doc,lista[index])

    #Funcion que guarda el document_bd en un pickle

    """
    
