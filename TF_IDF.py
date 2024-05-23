import re
import math
from limpieza import *

    #----Calculate term frecuency---
    #Primero: tokenizar palabras

def tokenizacion(texto):
    # Dividir el texto en tokens utilizando expresiones regulares
    tokens = re.findall(r'\b\w+\b', texto)
    return tokens

#Recibe una lista con los textos de cada documento por posicion
def Tf_Idf(documents):
    # Diccionario para almacenar la frecuencia de cada palabra en cada documento
    dictOfWords = {}
    for index, sentence in enumerate(documents): #enumerate devuelve la posicion de la lista (index) junto con su contenido (sentense)
        # Tokeniza las palabras en la oración
        tokenizeWords = tokenizacion(sentence)
        
        # Almacena las palabras y su frecuencia en el documento actual
        dictOfWords[index] = [(word, tokenizeWords.count(word)) for word in tokenizeWords]

    # Segundo: Eliminar duplicados
    # Diccionario para almacenar la frecuencia de términos sin duplicados en cada documento
    #unificar esta parte con la de tfidf de eliminado (marcado abajo a que me refiero)
    termFrequency = {}
    for i in range(len(documents)):
        listOfNoDuplicates = []
        for wordFreq in dictOfWords[i]:
            if not wordFreq in listOfNoDuplicates:
                listOfNoDuplicates.append(wordFreq)
        #Guarda las palabras y su frecuencia sin valores repetidos en "termFrequency" del documento "i"
        termFrequency[i] = listOfNoDuplicates

    # ---- Calcular TF ----
    # Tercero: Frecuencia de términos Normalizada
    # Diccionario para almacenar la frecuencia normalizada de términos en cada documento
    normalizedTermFrequency = {}
    for i in range(len(documents)):
        sentence = dictOfWords[i] #Guarda en "sentense" todas las palabras del documento "i"
        lenOfSentence = len(sentence) #Guarda la cantidad de palabras existentes en el documento "i" en la variable "lenOfSentence"
        listOfNormalized = []
        for wordFreq in termFrequency[i]:
            # Calcula la frecuencia normalizada dividiendo la frecuencia por el número total de palabras en la oración
            normalizedFreq = wordFreq[1] / lenOfSentence 
            listOfNormalized.append((wordFreq[0], normalizedFreq))
        normalizedTermFrequency[i] = listOfNormalized #Guarda las palabras del documento "i" con su respectivo valor TF

    # Cuarto: Juntar todas las oraciones y tokenizar las palabras
    # Guarda todos los textos de todos los documentos en una unica variable "allDocuments" y luego lo tokeniza 
    allDocuments = ''
    for sentence in documents:
        allDocuments += sentence + ' '
    allDocumentsTokenized = tokenizacion(allDocuments)

    # Eliminar duplicados de todas las palabras en los documentos
    #a esto me refiero arriba
    allDocumentsNoDuplicates = []
    #Elimina duplicados de la variable "allDocuments" y lo guarda en "allDocumentsNoDuplicates"
    for word in allDocumentsTokenized:
        if word not in allDocumentsNoDuplicates:
            allDocumentsNoDuplicates.append(word) 

    # Segundo: Calcular el número de documentos donde aparece cada término
    dictOfNumberOfDocumentsWithTermInside = {}
    for index, voc in enumerate(allDocumentsNoDuplicates): #enumerate devuelve la posicion de la lista (index) junto con su contenido (voc)
        count = 0
        for sentence in documents:
            if voc in sentence:
                count += 1
        #Guarda en "dictOfNumberOfDocumentsWithTermInside" las palabras junto con la cantidad de documentos que la contienen
        dictOfNumberOfDocumentsWithTermInside[index] = (voc,count) 

    # ---- Calcular IDF ----
    dictOFIDFNoDuplicates = {}
    for i in range(len(normalizedTermFrequency)):
        listOfIDFCalcs = []
        for word in normalizedTermFrequency[i]:
            for x in range(len(dictOfNumberOfDocumentsWithTermInside)):
                if word[0] == dictOfNumberOfDocumentsWithTermInside[x][0]:
                    # Calcular IDF utilizando la fórmula log(N/n)
                    listOfIDFCalcs.append((word[0], math.log(len(documents) / dictOfNumberOfDocumentsWithTermInside[x][1])))
        #Guarda en "dictOFIDFNoDuplicates" la misma lista de palabras que "normalizedTermFrequency" pero con su respectivo IDF
        dictOFIDFNoDuplicates[i] = listOfIDFCalcs
    ########alguna parte acá no usa los terminos eliminados (los duplicados), revisar eso
    # Multiplicar TF por IDF para obtener TF-IDF
    dictOFTF_IDF = {}
    for i in range(len(normalizedTermFrequency)):
        listOFTF_IDF = []
        TFsentence = normalizedTermFrequency[i]
        IDFsentence = dictOFIDFNoDuplicates[i]
        for x in range(len(TFsentence)):
            listOFTF_IDF.append((TFsentence[x][0], TFsentence[x][1] * IDFsentence[x][1]))
        #Guarda en "dictOFTF_IDF" las palabras del documento "i" con sus respectivos TF-IDF
        dictOFTF_IDF[i] = listOFTF_IDF

    #devuelve un diccionario donde cada posicion "i" es una lista de las palabras del documento "i" con su respectivo TF-IDF
    return dictOFTF_IDF 
    


"""
documents = ['the universe has very many stars',
             'the galaxi contains many stars',
             'the cold brezeze of winter made it very cold outside']


print(Tf_Idf(documents))
"""