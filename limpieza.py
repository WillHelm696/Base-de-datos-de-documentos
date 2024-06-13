import re
#from config import *

def leer_txt(item):
    with open(item,'r',encoding='utf-8') as archivo:
        text = archivo.read()
    return text

def clean_text(text):
  # Pasar el texto a minúsculas
  cleaned_text = text.lower()
 # Reemplazar letras con tilde por la misma letra sin tilde
  cleaned_text = re.sub(r'[áÁ]', 'a', cleaned_text)
  cleaned_text = re.sub(r'[éÉ]', 'e', cleaned_text)
  cleaned_text = re.sub(r'[íÍ]', 'i', cleaned_text)
  cleaned_text = re.sub(r'[óÓ]', 'o', cleaned_text)
  cleaned_text = re.sub(r'[úÚ]', 'u', cleaned_text)
  cleaned_text = re.sub(r'[ñÑ]', 'n', cleaned_text)

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
  cleaned_text = pattern.sub('', cleaned_text)

  # Eliminar espacios extra generados por las eliminaciones
  cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

  #limpieza para "stemming"
  cleaned_text=re.split(r'\s+', cleaned_text)

   #ver cuales si y cuales no
  sufijos_corto = [ 'o','r','er','es','as','s','ar', 'ir','bilidad','dad','dor','dora','dura','duria','ndo','res','mente',
                   'ado', 'ido', 'iendo', 'ando', 'arian', 'erian', 'irian',
                  'are', 'ere', 'ire', 'aria', 'eria', 'iria', 'aba', 'ia', 'aste', 'iste', 
                  'sion', 'xion', 'tad', 'tud', 'aje', 'ista', 'oso', 'osa', 'al', 'ario', 
                  'eza', 'ez', 'ible', 'able','ble','cion' ]
  
  for i in range(len(cleaned_text)):
    word = cleaned_text[i]
    for sufijo in sufijos_corto:
      if word.endswith(sufijo):
        if (len(word)-len(sufijo))>=4:
          word = word[:-len(sufijo)] #elimina el sufijo
        elif len(word)<=4 and len(sufijo)==1 and len(word)!=len(sufijo):
           word = word[:-len(sufijo)]
    cleaned_text[i]=word
  return cleaned_text
