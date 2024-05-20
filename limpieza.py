import re
from config import *
from trie_para_iftdf import *

def convert_to_trie(archivos):
    trie = Trie()
    for item in archivos:
        item=clean_text(item) #limpia el texto
        words = item.split() # Divide el texto en palabras
        for word in words:
            insert(trie, word)
    return trie


def clean_text(text):
  texto=leer_txt(text)
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
