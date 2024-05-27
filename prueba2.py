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
    insert_tokens(tokenized_docs)
    return

def insert_tokens(tokens):
    dict_trie={}
    for key in tokens:
        list_tokens = tokens[key]
        trie_words=Trie()
        for word in list_tokens:
            insert(trie_words,word)
            trie_words.root.all_words=len(list_tokens)
        dict_trie[key]=trie_words
    lista_keys=list(dict_trie.keys())
    print(lista_keys)
    #printTrie(dict_trie[lista_keys[0]].root)
    #print(dict_trie)
    print("probando print")
    root=dict_trie["El_Misterio_de_la_Fórmula_Perdida"].root
    #printTrie(root)
    print(root.all_words)
    
    return