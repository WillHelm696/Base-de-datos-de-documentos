import re
import math
from limpieza import *
from trie import *

#Tokenizar texto en palabras
# def tokenizacion(texto):
#     # Dividir el texto en tokens utilizando expresiones regulares
#     tokens = clean_text(texto)    
#     tokens = re.split(r'\s+', tokens)
#     return tokens

#Realiza la Tokenizacion sobre todos los documentos y consegue el universo de palabras
def tokenizeWords(documents):
    dictOfWords = {} # Diccionario para almacenar la frecuencia de cada palabra en cada documento
    allWordsOfText=[] #Lista que contrenda todo el documento vectorizado
    UniverseWords = {} #Diccionario que contendra todas las palabras que existen en nuestro universo
    if type(documents) is str:
        tokenizeWords = clean_text(documents)
        dictOfWords[0]={}
        for word in tokenizeWords:
            dictOfWords[0][word]=tokenizeWords.count(word)
            UniverseWords[word]=""
        allWordsOfText.append(tokenizeWords)
        return (dictOfWords,allWordsOfText,UniverseWords)
    else:
        for index, sentence in enumerate(documents): #enumerate devuelve la posicion de la lista (index) junto con su contenido (sentense)
            # Tokeniza las palabras en la oración
            tokenizeWords = clean_text(sentence)
            dictOfWords[index]={}
            # Almacena las palabras y su frecuencia en el documento actual
            for word in tokenizeWords:
                dictOfWords[index][word]=tokenizeWords.count(word)
                UniverseWords[word]=""
            allWordsOfText.append(tokenizeWords)

#Retorna un diccionario con todos los documentos Tokenizados, una lista con todos los textos vectorizados 
#de cada documento y un diccionario de todas las palabras que existen en nuestro universo, ambos devueltos en una tupla
    return (dictOfWords,allWordsOfText,UniverseWords)

#Recibe un diccionario con los textos de cada documento por posicion
#Retoruna un diccionario donde cada posicion es el documento "i" y dentro tiene un diccionario con todas sus palabras junto con su TF
def Tf(dictOfWords,allWordsOfTexts):
    # ---- Calcular TF ----
    # Frecuencia de términos Normalizada
    docTokenizedTF = {} # Diccionario para almacenar la frecuencia normalizada de términos en cada documento
    for i in range(len(dictOfWords)):
        sentence = allWordsOfTexts[i] #Guarda en "sentense" todas las palabras del documento "i"
        lenOfSentence = len(sentence) #Guarda la cantidad de palabras existentes en el documento "i" en la variable "lenOfSentence"
        docTokenizedTF[i]={}
        for wordFreq in dictOfWords[i]:
            # Calcula la frecuencia normalizada dividiendo la frecuencia por el número total de palabras en la oración
            normalizedFreq = dictOfWords[i][wordFreq] / lenOfSentence 
            docTokenizedTF[i][wordFreq]=normalizedFreq
    return docTokenizedTF

def Tf_Idf(docTokenized,UniverseWords):
    # Calcular el número de documentos donde aparece cada término
    numOfWordsInDocuments = {}
    docTokenizedTF={}
    for item in docTokenized:
        if type(docTokenized[item]) != dict:
            docTokenizedTF[item]=get_words(docTokenized[item].root) #devuelve trie como diccionario
            #diccionario_frecuencias_totales[item] = docTokenizedTF[item].root.palabras_totales
    for word in UniverseWords.keys(): 
        count = 0
        for item in docTokenizedTF:
            if word in docTokenizedTF[item]:
                count += 1
    #Guarda en "numOfWordsInDocuments" el universo de palabras junto con la cantidad de documentos que la contienen
        numOfWordsInDocuments[word] = count
    # ---- Calcular IDF ----
    dictOFIDFNoDuplicates = {}
    for item in docTokenizedTF:
        dictOFIDFNoDuplicates[item]={}
        for word in docTokenizedTF[item]:
            # Calcular IDF utilizando la fórmula log(N/n)
            dictOFIDFNoDuplicates[item][word]=math.log(len(docTokenizedTF)/numOfWordsInDocuments[word])
        #Guarda en "dictOFIDFNoDuplicates" la misma lista de palabras que "docTokenizedTF" pero con su 
        #respectivo IDF
    #Multiplicar TF por IDF para obtener TF-IDF
    dictOFTF_IDF = {}
    for item in docTokenizedTF:
        dictOFTF_IDF[item]={}
        for word in docTokenizedTF[item]:
            #dictOFTF_IDF[item][word]=docTokenizedTF[item][word]*dictOFIDFNoDuplicates[item][word]
            dictOFTF_IDF[item][word]=(docTokenizedTF[item][word]/docTokenized[item].root.palabras_totales)*dictOFIDFNoDuplicates[item][word]
    #Guarda en "dictOFTF_IDF" las palabras del documento "item / nombre" con sus respectivos TF-IDF y lo devuelve
    return dictOFTF_IDF 
