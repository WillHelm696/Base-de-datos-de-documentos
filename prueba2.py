from config import *
import re
import math
def tokenizacion(texto):
    # Dividir el texto en tokens utilizando expresiones regulares
    tokens = re.findall(r'\b\w+\b', texto)
    return tokens

def Tf_Idf2(documents):
    # Diccionario para almacenar la frecuencia de cada palabra en cada documento
    dictOfWords = {}
    for index, sentence in enumerate(documents):
        # Tokeniza las palabras en la oración
        tokenizeWords = tokenizacion(sentence)
        print("probando pt1")
        print(tokenizeWords)
        # Almacena las palabras y su frecuencia en el documento actual
        dictOfWords[index] = [(word, tokenizeWords.count(word)) for word in tokenizeWords]
        print("probando pt2")
        print(dictOfWords)

    # Segundo: Eliminar duplicados
    # Diccionario para almacenar la frecuencia de términos sin duplicados en cada documento

    termFrequency = {}
    for i in range(len(documents)):
        listOfNoDuplicates = []
        for wordFreq in dictOfWords[i]:
            listOfNoDuplicates.append(wordFreq)
        termFrequency[i] = listOfNoDuplicates
    # Tercero: Frecuencia de términos Normalizada
    # Diccionario para almacenar la frecuencia normalizada de términos en cada documento
    normalizedTermFrequency = {}
    for i in range(len(documents)):
        sentence = dictOfWords[i]
        lenOfSentence = len(sentence)
        print("probando pt3")
        print(lenOfSentence)
        listOfNormalized = []
        for wordFreq in termFrequency[i]:
            # Calcula la frecuencia normalizada dividiendo la frecuencia por el número total de palabras en la oración
            normalizedFreq = wordFreq[1] / lenOfSentence
            listOfNormalized.append((wordFreq[0], normalizedFreq))
        normalizedTermFrequency[i] = listOfNormalized
        print("probando pt4")
        print(normalizedTermFrequency)
    # ---- Calcular IDF ----
    # Cuarto: Juntar todas las oraciones y tokenizar las palabras
    allDocuments = ''
    for sentence in documents:
        allDocuments += sentence + ' '
    allDocumentsTokenized = tokenizacion(allDocuments)
    print("probando pt5")
    print(allDocumentsTokenized)

    # Eliminar duplicados de todas las palabras en los documentos
    allDocumentsNoDuplicates = []
    for word in allDocumentsTokenized:
        if word not in allDocumentsNoDuplicates:
            allDocumentsNoDuplicates.append(word)
    print("probando pt6")
    print(allDocumentsNoDuplicates)
    # Segundo: Calcular el número de documentos donde aparece cada término
    dictOfNumberOfDocumentsWithTermInside = {}
    for index, voc in enumerate(allDocumentsNoDuplicates):
        count = 0
        for sentence in documents:
            if voc in sentence:
                count += 1
        dictOfNumberOfDocumentsWithTermInside[index] = (voc, count)
    print("probando pt7")
    print(dictOfNumberOfDocumentsWithTermInside)
    # Calcular IDF
    dictOFIDFNoDuplicates = {}
    for i in range(len(normalizedTermFrequency)):
        listOfIDFCalcs = []
        for word in normalizedTermFrequency[i]:
            for x in range(len(dictOfNumberOfDocumentsWithTermInside)):
                if word[0] == dictOfNumberOfDocumentsWithTermInside[x][0]:
                    # Calcular IDF utilizando la fórmula log(N/n)
                    listOfIDFCalcs.append((word[0], math.log(len(documents) / dictOfNumberOfDocumentsWithTermInside[x][1])))
        dictOFIDFNoDuplicates[i] = listOfIDFCalcs

    # Multiplicar TF por IDF para obtener TF-IDF
    dictOFTF_IDF = {}
    for i in range(len(normalizedTermFrequency)):
        listOFTF_IDF = []
        TFsentence = normalizedTermFrequency[i]
        IDFsentence = dictOFIDFNoDuplicates[i]
        for x in range(len(TFsentence)):
            listOFTF_IDF.append((TFsentence[x][0], TFsentence[x][1] * IDFsentence[x][1]))
        dictOFTF_IDF[i] = listOFTF_IDF

    print("probando pt8")
    print(dictOFTF_IDF)
    print("fin prueba")
    return dictOFTF_IDF