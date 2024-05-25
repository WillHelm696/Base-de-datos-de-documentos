from config import *
from main import *
from limpieza import *
from TF_IDF import *
import numpy as np
from similitud_coseno import *
from ranking import *

texto1="los perros son muy bonitos"
texto2="los perros corren rapido y ladran"
texto3="los gatos comen pescado"
texto4="Los perros comen carne"
#texto1=clean_text(texto1)
#texto2=clean_text(texto2)
documents=[texto1,texto2,texto3,texto4]
#print("Tokenizacion")
documents_tokenizados=tokenizeWords(documents)
#print(documents_tokenizados)
#print("calcular TF")
allWords=documents_tokenizados[1]
documents_tokenizados_tf=Tf(documents_tokenizados[0],allWords)
#print("docTokenizedTF es: ")
#for i in range(0,len(documents_tokenizados_tf)):
#     print(i," ",documents_tokenizados_tf[i])

'''
print("calcular TF-IDF")
universo=documents_tokenizados[2]
tfidf=Tf_Idf(documents_tokenizados_tf,universo)
for i in range(0,len(tfidf)):
     print(i," ",tfidf[i])
'''
text1=documents_tokenizados_tf[0]
text2=documents_tokenizados_tf[1]
#text1=tfidf[0]
#text2=tfidf[1]
docs={}
docs[0]=text1
docs[1]=text2
docs[2]=documents_tokenizados_tf[2]
docs[3]=documents_tokenizados_tf[3]


"""def vector_module(text):
    mod=0
    for word in text:
        mod+=text[word]*text[word]
    mod=np.sqrt(mod)
    return mod"""

"""def cosine_similarity(text1,text2):
  if text1 == text2:
    return 1.0
  mod1=vector_module(text1)
  mod2=vector_module(text2)
  if mod1==0 or mod2==0:
      return 0
  sumxy = 0
  for i in text1:
        sumxy += text1[i]*text2[i]
  return sumxy/(mod1*mod2)"""
doc_comp=comparetexts(text2,docs)

print(doc_comp)
#text1=doc_comp[3]
#print(text1)

#print("similitud coseno")
#print(cosine_similarity(doc_comp[2],doc_comp[1]))

print("ranking")
ranking_docs=ranking(doc_comp[2],doc_comp)

print(ranking_docs)













