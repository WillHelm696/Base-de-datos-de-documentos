from TF_IDF import *
from limpieza import *
from similitud_coseno import *
from ranking import *
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


def bd_documents(lista):
    documents = []
    for item in lista:

        if item.endswith(".pdf"):
            text = leer_pdf(item)
        elif item.endswith(".txt"):
            text = leer_txt(item)
        
        text = clean_text(text)
        documents.append(text)

    file_names = [os.path.splitext(os.path.basename(item))[0] for item in lista]
    rutas_textos = {item: contenido for item, contenido in zip(file_names, lista)}
    #print("Creando base de datos", rutas_textos)
    #Calcula para documento el tf-ydf de cada palabra y lo guardacomo tupla
    docTokenized_UniverseWords=tokenizeWords(documents)
    docTokenized=docTokenized_UniverseWords[0] #obtenemos nuestros documentos tokenizados en un diccionario
    allWordsOfTexts=docTokenized_UniverseWords[1] #obtenemos una lista de los documentos tokenizados

    UniverseWords=docTokenized_UniverseWords[2] #obtenemos nuestro universo de palabras
    docTokenizedTF2=Tf(docTokenized,allWordsOfTexts) #Calculamos TF a cada palabra de nuestros documentos
    #guardar como hash usando el nombre del archivo como key
    docTokenizedTF = {}
    
    for i, item in enumerate(file_names):
        docTokenizedTF[item] = docTokenizedTF2[i]

    save_file(UniverseWords, "UniverseWords")
    save_file(docTokenizedTF, "docTokenizedTF")
    save_file(rutas_textos, "rutas_textos")
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
    UniverseWords=file_upload("UniverseWords") #words sin tf, limpias
    docTokenizedTF=file_upload("docTokenizedTF") #lista de docs tokenizados con tf, usar nombre como key 
    rutas_textos=file_upload("rutas_textos") #rutas de los textos
    #print("Probando doctokenized", type(docTokenizedTF),docTokenizedTF.keys(), docTokenizedTF)
    textoProfeTokenizado_Universo=tokenizeWords(textoProfe)
    #print("Texto del profesor tokenizado y universo de palabras es: ",textoProfeTokenizado_Universo)

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
    ##docTokenizedTF[len(docTokenizedTF)]=textoProfeTF[0]
    docTokenizedTF[len(docTokenizedTF)] = textoProfeTF[0]
    # print(" ")
    # print("Agregando el texto del profe tokenizado a la lista de documentos queda: ")
    # print(docTokenizedTF)
    # print(" ")

    #print("Texto del profesor tokenizado es: ",textoProfeTF)

    ##docTokenizedTF_IDF=Tf_Idf(docTokenizedTF,UniverseWords)
    docTokenizedTF_IDF=Tf_Idf(docTokenizedTF,UniverseWords)
    #print("docTokenizedTF_IDF es: ")
    #for i in range(0,len(docTokenizedTF_IDF)):
    #print(docTokenizedTF_IDF)

    comparacion=comparetexts(textoProfeTF[0],docTokenizedTF_IDF)
    print("Ranking")
    ranked_docs=ranking(textoProfeTF[0],docTokenizedTF_IDF,rutas_textos)
    print(ranked_docs)