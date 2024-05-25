import re
from config import *
from trie_para_iftdf import *


def leer_txt(item):
    with open(item,'r',encoding='utf-8') as archivo:
        text = archivo.read()
    return text

def convert_to_trie(archivos):
    trie = Trie()
    for item in archivos:
        item=clean_text(item) #limpia el texto
        words = item.split() # Divide el texto en palabras
        for word in words:
            insert(trie, word)
    return trie


def clean_text(text):
  #texto=leer_txt(text)
  # Pasar el texto a minúsculas
  texto = text.lower()
  #print("aiuda",texto)
 # Reemplazar letras con tilde por la misma letra sin tilde
  cleaned_text = re.sub(r'[áÁ]', 'a', texto)
  cleaned_text = re.sub(r'[éÉ]', 'e', cleaned_text)
  cleaned_text = re.sub(r'[íÍ]', 'i', cleaned_text)
  cleaned_text = re.sub(r'[óÓ]', 'o', cleaned_text)
  cleaned_text = re.sub(r'[úÚ]', 'u', cleaned_text)

  # Eliminar símbolos y números usando una expresión regular
  cleaned_text = re.sub(r'[^a-zA-Z\s]', '', cleaned_text)

  words_to_remove={'si', 'a','sr','sra','sres','pues','sta','aca','ahi','ti','aun','conmigo','cada','aunque','asi','atras','al','alla', 'ante','antes', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 'en', 'entre', 'hacia', 'hasta', 
                 'mediante', 'para', 'por', 'pro','segun', 'sin', 'so', 'sobre', 'tras', 'versus','via', 'la','las','el','los','ella','ellos','yo'
                 ,'nosotros','vosotros','vaya','vamos','vais','va','van','voy','ustedes','usted','tu','vos','ellas','este','estos','esta','estas','esa','eso','esas','esos',
                 'aquellos','aqui','quien','quienesquiera','quienes','quienquiera','arriba','aquella','aquello','aquellas','aquel','mio','mi','tuyo','tu','tus','su','sus','nuestro','nos','le','suyo','suyos','mios','mia','mias','vuestro',
                 'tuya','tuyo','tuyos','tuyas','nuestra', 'nuestros','nuestras','suya','suyas','vuestra','vuestras','vuestros','esto','les','y','o',
                 'que','como','te','se','lo','le','nos','me','se','mi','su','nuestro','vuestro','tuyo','suyo','nuestro','vuestro',
                 'unos','unas','una','unos','otros','otras','otra','otro','soy','eres','es','somos','sois','son','estoy','estamos'
                 ,'un'}
    # Crear un patrón de expresión regular que coincida con las palabras a eliminar
  pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in words_to_remove) + r')\b', re.IGNORECASE)
  
  # Usar la función sub de re para reemplazar las palabras no deseadas con una cadena vacía
  cleaned_text = pattern.sub('', texto)

  # Eliminar espacios extra generados por las eliminaciones
  cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
  return cleaned_text
