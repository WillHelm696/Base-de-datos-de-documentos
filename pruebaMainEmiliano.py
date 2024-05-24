from config import *
from prueba2 import *
from TF_IDF import *
import argparse
import sys
#from limpieza import *

documents=["Al perro le gusta la carne perro","Al gato le gusta la carne gusta","El gato y el perro se odian","El gato caza pajaros"]

textoProfe=["Al pajaro le gusta las migajas de pan"]

#Tokenizamos los documentos
docTokenized_UniverseWords=tokenizeWords(documents)
docTokenized=docTokenized_UniverseWords[0] #obtenemos nuestros documentos tokenizados en un diccionario
allWordsOfTexts=docTokenized_UniverseWords[1] #obtenemos una lista de los documentos tokenizados
UniverseWords=docTokenized_UniverseWords[2] #obtenemos nuestro universo de palabras
docTokenizedTF=Tf(docTokenized,allWordsOfTexts) #Calculamos TF a cada palabra de nuestros documentos
# print("docTokenized es: ")
# for i in range(0,len(docTokenized)):
#     print(i," ",docTokenized[i])
# print(" ")
# print("docTokenizedTF es: ")
# for i in range(0,len(docTokenizedTF)):
#     print(i," ",docTokenizedTF[i])

#LLEGA EL MENSAJE DEL PROFE

#Tokenizamos el texto del profe

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


