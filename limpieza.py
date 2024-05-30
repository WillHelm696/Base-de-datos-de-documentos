import re
from config import *

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
#depende del sufijo cambiar una letra? ej: alteracion --> altera --> alterar, por casos como "aldeano" --> "alde" --> aldea / "ciudadano --> "ciudad
# "ero" cambiar por final de palabra o que hacer?  guerrilero --> guerrilla zapatero --> zapato? 
#eza de tristeza por ej
#ido / ida comido com por ej
#"er " / r
#es / s
  cleaned_text=re.split(r'\s+', cleaned_text)

  sufijos = [
    'aceo', 'acea', 'aco', 'aca', 'ada', 'ado', 'ada', 'aje', 'al', 'algia', 'amen', 
    'ancia', 'ano', 'ana', 'anza', 'ar', 'ario', 'aria', 'arquia', 'ata', 'ato', 'avo', 
    'ava', 'azgo', 'azo', 'bilidad', 'ble', 'cardio', 'cardia', 'cida', 'cidio', 'cion', 
    'cola', 'cracia', 'crata', 'cultor', 'cultora', 'dad', 'demia', 'dero', 'dera', 'dizo', 
    'diza', 'dor', 'dora', 'dura', 'ear', 'ecer', 'eco', 'edo', 'eda', 'edro', 'ego', 'ega', 
    'encia', 'eno', 'ena', 'ense', 'eno', 'ena', 'era', 'eria', 'ero', 'era', 'es', 'esa', 
    'esco', 'esca', 'ez', 'eza', 'fagia', 'fago', 'faga', 'fero', 'fera', 'filia', 'filo', 
    'fila', 'fito', 'fobia', 'fobo', 'foba', 'fono', 'fona', 'fonia', 'forme', 'fugo', 
    'fuga', 'gamia', 'gamo', 'gama', 'genia', 'geno', 'gena', 'geo', 'ginia', 'gino', 
    'gina', 'gono', 'grafia', 'grafo', 'grafa', 'grama', 'i', 'ia', 'iano', 'iana', 'ica', 
    'ido', 'ida', 'ificar', 'il', 'in', 'ina', 'ina', 'ing', 'ismo', 'ista', 'istico', 
    'istica', 'itis', 'izar', 'izo', 'iza', 'ita', 'latra', 'latria', 'lisis', 'lito', 
    'logia', 'logo', 'loga', 'illos', 'mancia', 'mania', 'mano', 'mana', 'mante', 'mente', 
    'mento', 'metria', 'metro', 'miento', 'nomia', 'nomo', 'noma', 'nte', 'oide', 'oleo', 
    'oma', 'ope', 'opia', 'osis', 'oso', 'osa', 'on', 'ona', 'or', 'pata', 'patia', 
    'pedia', 'podo', 'polis', 'teca', 'torio', 'tud', 'udo', 'uda', 'ura', 'ucho', 
    'ucha', 'voro', 'vora'
  ]

  """for word in cleaned_text:
    for suffix in sufijos:
      if word.endswith(suffix):
        word=re.sub(f'{suffix}$', '', word)
"""
  for i in range(len(cleaned_text)):
    word = cleaned_text[i]
    for sufijo in sufijos:
      if word.endswith(sufijo):
        cleaned_text[i] = word[:-len(sufijo)] #elimina el sufijo

  print(cleaned_text)

  return cleaned_text
