from trie import *
from TF_IDF import *
from limpieza import *
from similitud_coseno import *
from ranking import *
import os
import pickle
import PyPDF2
import time
def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    """
    Llama en un bucle para crear una barra de progreso terminal
    @params:
        iteration   - Requerido  : iteración actual (Int)
        total       - Requerido  : total de iteraciones (Int)
        prefix      - Opcional   : prefijo de la cadena (Str)
        suffix      - Opcional   : sufijo de la cadena (Str)
        decimals    - Opcional   : número de decimales en porcentaje (Int)
        length      - Opcional   : longitud de la barra (Int)
        fill        - Opcional   : barra de llenado del carácter (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    # Imprimir nueva línea cuando se completa
    if iteration == total: 
        print()

# Guarda en una lista las rutas de los archivos 
def load_file(ruta):
    lista = os.listdir(ruta)
    archivos = []
    #recorre cada archivo y carpeta en la ruta

    total_files = len(lista)

    for i, item in enumerate(lista) :
        contenido = os.path.join(ruta,item)
        if os.path.isfile(contenido):
            archivos.append(contenido)
        elif os.path.isdir(contenido):
            #Si hay una carpeta agrega los archivos de la carpeta a la lista
            archivos += load_file(contenido)
        """
        # Actualiza la barra de progreso
        print_progress_bar(i + 1, total_files, prefix='Cargando archivos:', suffix='Completado', length=50)
        time.sleep(0.1) # Simula el tiempo de procesamiento
        """
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
    # Guardar los nuevos datos como un archivo nuevo
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)
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


def create_db(lista):
    #crea una lista de documentos limpios
    documents = []
    
    total_files = len(lista)
    print()
    for i, item in enumerate(lista):
        if item.endswith(".pdf"):
            text = leer_pdf(item)
        elif item.endswith(".txt"):
            text = leer_txt(item)
        text = clean_text(text)
        documents.append(text)
        """
        # Actualiza la barra de progreso
        print_progress_bar(i + 1, total_files, prefix='Generando Base De Datos:', suffix='Completado', length=50)
        time.sleep(0.1) # Simula el tiempo de procesamiento
        """
    file_names = [os.path.splitext(os.path.basename(item))[0] for item in lista] #guarda los nombres para usarlos de key
    rutas_textos = {item: contenido for item, contenido in zip(file_names, lista)} #guarda las rutas
    #tokeniza los documentos
    tokenized_docs = {}
    for i, item in enumerate(file_names):
        tokenized_docs[item]=documents[i]
   
#devuelve un diccionario con los tries de cada documento y un trie con todas las palabras de todos los documentos    
    tokens_trie=insert_tokens(tokenized_docs)
    #guardar info cant total palabras por doc (contar frecuencias)
    tokenized_docs=tokens_trie[0]
    universe_trie=tokens_trie[1]
    #guarda los archivos 
    save_file(universe_trie, "universe_trie")
    save_file(tokenized_docs, "tokenized_docs")
    save_file(rutas_textos, "rutas_textos")

    print('\n')
    print("document data-base created successfully")
    print('\n')
    return
    
def search(input):

    # Verificar si los archivos necesarios existen en la base de datos
    required_files = ["universe_trie", "tokenized_docs", "rutas_textos"]
    missing_files = [file for file in required_files if not os.path.exists(f"database/{file}.pkl")]

    if missing_files:
        print('\n')
        print("Por favor, cargue los archivos en la base de datos primero.")
        print('\n')
        return

     #Cargar archivos guardados en database
    universe_trie=file_upload("universe_trie") 
    tokenized_docs=file_upload("tokenized_docs")
    rutas_textos=file_upload("rutas_textos")
    #procesar texto entrada 
    input=tokenizeWords(input)
    input_tokenized= input[0]
    #agregar palabras input al universo
    for word in input_tokenized[0]:
        insert(universe_trie,word)
    #calcular tf de las palabras del input
    tf_input=Tf(input_tokenized, input[1][0])
    #Agrego el texto del profesor tokenizado a la lista de documentos y calculo tf-idf para todos los docs
    tokenized_docs[len(tokenized_docs)] = tf_input[0]
    universe_words=get_words(universe_trie.root) #devuelve trie como diccionario
    tf_idf_docs=Tf_Idf(tokenized_docs,universe_words)
    #ranking
    ranking(tf_input[0],tf_idf_docs,rutas_textos)
    return

#recibe un diccionario con tf-idf del profe, y un hash de hash con tf-idf de todos los documentos  
def comparetexts_new(input_text,allDocuments):
    documents_compared={} #dict que guarda todos los documentos vectorizados en base al texto entrada
    for doc in allDocuments:
        document=allDocuments[doc] #accedo al dict del documento 
        document=get_words(document)
        doc_vector={}
        for word in document: #verifico cada palabra del dict del documento si se encuentra en el texto ingresado por el profesor
            if word in input_text:
                 doc_vector[word]=input_text[word] #si se encuentra la palabra se toma su tf
            else:
                 doc_vector[word]=0.0 #sino, es cero
        documents_compared[doc]=doc_vector #agregar el vector al diccionario
    return documents_compared

#recibe los tokens de los documentos y los inserta en un trie, devuelve un diccionario con los tries de cada documento
#y un trie con todas las palabras de todos los documentos
def insert_tokens(tokens):
    dict_trie={}
    universe_trie=Trie()
    for key in tokens:
        #por cada documento se crea un trie y se insertan las palabras
        list_tokens = tokens[key]
        trie_words=Trie()
        for word in list_tokens:
            insert(trie_words,word)
            insert(universe_trie,word) #inserto todas las palabras en trie universal
        dict_trie[key]=trie_words
    return (dict_trie,universe_trie)     