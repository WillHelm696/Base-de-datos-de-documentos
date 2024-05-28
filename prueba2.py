from Trie2 import *
from TF_IDF import *
from limpieza import *
from similitud_coseno import *
from ranking import *
from config import *
import os
import pickle
import PyPDF2

def new_bd(lista):
    #crea una lista de documentos limpios
    documents = []
    for item in lista:
        if item.endswith(".pdf"):
            text = leer_pdf(item)
        elif item.endswith(".txt"):
            text = leer_txt(item)
        
        text = clean_text(text)
        documents.append(text)
    file_names = [os.path.splitext(os.path.basename(item))[0] for item in lista] #guarda los nombres para usarlos de key
    rutas_textos = {item: contenido for item, contenido in zip(file_names, lista)} #guarda las rutas
    #tokeniza los documentos
    tokenized_docs = {}
    for i, item in enumerate(file_names):
        tokens=documents[i]
        tokenized_docs[item]=re.split(r'\s+', tokens)
    #tokeniza, calcula tf y devuelve universe words
    tokens_trie=insert_tokens(tokenized_docs)
    tokenized_docs_tf=tokens_trie[0]
    uninverse_trie=tokens_trie[1]
    save_file(uninverse_trie, "universe_trie")
    save_file(tokenized_docs_tf, "tokenized_docs_tf")
    save_file(rutas_textos, "rutas_textos")
    
    print('\n')
    print("document data-base created successfully")
    print('\n')
    return

def new_search(input):
    #Cargar archivos guardados en database
    #print("holis")
    universe_trie=file_upload("universe_trie") 
    tokenized_docs_tf=file_upload("tokenized_docs_tf")
    rutas_textos=file_upload("rutas_textos")
    #procesar texto entrada 
    input=tokenizeWords(input)
    input_tokenized= input[0]
    #print(input_tokenized)
    #agregar palabras input al universo
    for word in input_tokenized[0]:
        insert(universe_trie,word)
    #calcular tf de las palabras del input
    #print(type(input[1][0]))
    tf_input=Tf(input_tokenized, input[1][0])
    #Agrego el texto del profesor tokenizado a la lista de documentos
    print(tokenized_docs_tf)
    tokenized_docs_tf[len(tokenized_docs_tf)] = tf_input[0]
    universe_words=get_words(universe_trie.root)
    #print(type(tokenized_docs_tf), tokenized_docs_tf)
    tf_idf_docs=Tf_Idf(tokenized_docs_tf,universe_words)

    print("Ranking")
    ranked_docs=ranking(tf_input[0],tf_idf_docs,rutas_textos)
    #ranked_docs = ranked_docs[1:] #elimina el primer elemento (el mismo texto del profesor)
    if len(ranked_docs)<10: #como es top 10 si hay menos de 10 documentos se muestra solo los que hay
        for i in range(0,len(ranked_docs)):
            #agrega el texto al ranking
            path=ranked_docs[i][2]
            if path.endswith(".pdf"):
                text = leer_pdf(path)
            elif path.endswith(".txt"):
                text = leer_txt(path)
            ranked_docs[i] = ranked_docs[i][:3] + (text,) + ranked_docs[i][4:]
    else:
        for i in range(0,10): #si hay mas de 10 documentos se muestra solo los 10 primeros
            path=ranked_docs[i][2]
            if path.endswith(".pdf"):
                text = leer_pdf(path)
            elif path.endswith(".txt"):
                text = leer_txt(path)
            ranked_docs[i] = ranked_docs[i][:3] + (text,) + ranked_docs[i][4:]
            
    for index in ranked_docs:
        print("---------------------------------------------------------------------------------------------")
        print('\n')
        print(f"frecuencia: {index[0]}")
        print('\n')
        print(f"titulo: {index[1]}")
        print('\n')
        print(f"Direccion: {index[2]}")
        print('\n')
        print(index[3])


    return



#recibe un hash con tf-idf del profe, y un hash de hash con tf-idf de todos los documentos  
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