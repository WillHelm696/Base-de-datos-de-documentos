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
    #print(tokenized_docs)
    tokens_trie=insert_tokens(tokenized_docs)
    tokenized_docs_tf=tokens_trie[0]
    all_words=tokens_trie[1]
    save_file(all_words, "all_words")
    save_file(tokenized_docs_tf, "tokenized_docs_tf")
    save_file(rutas_textos, "rutas_textos")
    
    print('\n')
    print("document data-base created successfully")
    print('\n')
    return

def new_search(input):
    #Cargar archivos guardados en database
    print("holis")
    all_words=file_upload("all_words") 
    tokenized_docs_tf=file_upload("tokenized_docs_tf")
    rutas_textos=file_upload("rutas_textos")

    input_cleaned=clean_text(input)
    input_tokenized= re.split(r'\s+', input_cleaned)
    input_trie=Trie()
    for word in input_tokenized:
        insert(input_trie,word)
    #printTrie(input_trie.root)
    return



#recibe un hash con tf-idf del profe, y un hash de hash con tf-idf de todos los documentos  
def comparetexts_new(input_text,allDocuments):
    documents_compared={} #dict que guarda todos los documentos vectorizados en base al texto entrada
    for doc in allDocuments:
        document=allDocuments[doc] #accedo al dict del documento 
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
        list_tokens = tokens[key]
        trie_words=Trie()
        for word in list_tokens:
            insert(trie_words,word)
            insert(universe_trie,word)
            #trie_words.root.all_words=len(list_tokens)
            #universe_trie.root.all_words+=len(list_tokens)
        dict_trie[key]=trie_words
    lista_keys=list(dict_trie.keys())
    #print(lista_keys)
    #printTrie(dict_trie[lista_keys[0]].root)
    #print(dict_trie)
    #print("probando print")
    root=dict_trie["El_Misterio_de_la_Fórmula_Perdida"].root
    #printTrie(root)
    #print(root.all_words)
    #print(get_words(root))
    
    return (dict_trie,universe_trie)