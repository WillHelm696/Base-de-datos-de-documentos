words_to_remove={'si', 'a', 'sí', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 'en', 'entre', 'hacia', 'hasta', 
                 'mediante', 'para', 'por', 'pro','según', 'sin', 'so', 'sobre', 'tras', 'versus','vía', 'la','las','el','los'
                 'él','ella','ellos','yo','nosotros','vosotros','ustedes','usted','tú','vos','ellas','este','estos','ésta','esta','éste','éstas','esa','eso','esas','esos',
                 'aquellos','aquella','aquello','aquellas','aquel','mío','mi','tuyo','tu','tus','su','sus','nuestro','nos','le','suyo','suyos','míos','mía','mías','vuestro',
                 'tuya','tuyo','tuyos','tuyas','nuestra', 'nuestros','nuestras','suya','suyas','vuestra','vuestras','vuestros','ésto','les','y','o'}
def clean_text(text, words_to_remove):
    # Crear un patrón de expresión regular que coincida con las palabras a eliminar
    pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in words_to_remove) + r')\b', re.IGNORECASE)
    
    # Usar la función sub de re para reemplazar las palabras no deseadas con una cadena vacía
    cleaned_text = pattern.sub('', text)
    
    # Eliminar espacios extra generados por las eliminaciones
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text
