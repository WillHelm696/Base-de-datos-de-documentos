from TF_IDF import *
import re
import os
import pickle
import PyPDF2

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

#Funcion que guarda archivo en un pickle en la carpeta database
def save_file(data, file_name, save_path='database/'):
    # Verificar si la carpeta existe, si no, crearla
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # Guardar el archivo en la carpeta database
    file_path = os.path.join(save_path, file_name + '.pkl')

    # Verificar si el archivo ya existe
    if os.path.exists(file_path):
        # Si el archivo existe, borrarlo
        os.remove(file_path)
        #print(f"File '{file_name}.pkl' already exists. Overwriting...")

    # Guardar los nuevos datos como un archivo nuevo
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)
    #print(f"New file '{file_name}.pkl' saved successfully in database folder.")
    

# Cargar el archivo desde la carpeta database
def file_upload(file_name, load_path='database/'):
    file_path = os.path.join(load_path, file_name + '.pkl')
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data

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
    docTokenized_UniverseWords=tokenizeWords(documents)
    docTokenized=docTokenized_UniverseWords[0] #obtenemos nuestros documentos tokenizados en un diccionario
    allWordsOfTexts=docTokenized_UniverseWords[1] #obtenemos una lista de los documentos tokenizados

    UniverseWords=docTokenized_UniverseWords[2] #obtenemos nuestro universo de palabras
    docTokenizedTF=Tf(docTokenized,allWordsOfTexts) #Calculamos TF a cada palabra de nuestros documentos
    
    save_file(UniverseWords, "UniverseWords")
    save_file(docTokenizedTF, "docTokenizedTF")
    print('\n')
    print("document data-base created successfully")
    print('\n')
    
    """
    print("docTokenized es: ")
    for i in range(0,len(docTokenized)):
        print(i," ",docTokenized[i])
    print(" ")
    print("docTokenizedTF es: ")
    for i in range(0,len(docTokenizedTF)):
        print(i," ",docTokenizedTF[i])
    """ 
def search(textoProfe):

    #Cargar archivos guardados en datbase
    UniverseWords=file_upload("UniverseWords")
    docTokenizedTF=file_upload("docTokenizedTF")

    textoProfeTokenizado_Universo=tokenizeWords(textoProfe)

    textoProfeTokenizado = textoProfeTokenizado_Universo[0] #obtenemos el texto tokenizado en un diccionario

    todoTextoProfe = textoProfeTokenizado_Universo[1] #Texto vectorizado del profesor

    universoTextoProfe = textoProfeTokenizado_Universo[2] #obtenemos el universo de palabras del texto

    #Guardamos el universo de las palabras del texto en el universo de las palabras de documentos
    for word in universoTextoProfe:
        if word not in UniverseWords:
            UniverseWords[word]=""
    # print(" ")
    # print("UniverseWord agregando las nuevas palabras es: ")
    # print(UniverseWords)
    # print(" ")

    textoProfeTF=Tf(textoProfeTokenizado,todoTextoProfe) #obtenemos el texto tokenizado con su respectivo TF

    #Agrego el texto del profesor tokenizado a la lista de documentos
    docTokenizedTF[len(docTokenizedTF)]=textoProfeTF[0]
    # print(" ")
    # print("Agregando el texto del profe tokenizado a la lista de documentos queda: ")
    # print(docTokenizedTF)
    # print(" ")

    docTokenizedTF_IDF=Tf_Idf(docTokenizedTF,UniverseWords)
    print("docTokenizedTF_IDF es: ")
    for i in range(0,len(docTokenizedTF_IDF)):
        print(i," ",docTokenizedTF_IDF[i])