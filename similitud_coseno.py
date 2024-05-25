import numpy as np

#se podría recibir los dos textos y hacer la suma acá tambien para no recorrer dos veces cada texto
def vector_module(text):
    mod=0
    for word in text:
        mod+=text[word]*text[word]
    mod=np.sqrt(mod)
    return mod

def cosine_similarity(text1,text2):
  if text1 == text2:
    return 1.0
  mod1=vector_module(text1)
  mod2=vector_module(text2)
  if mod1==0 or mod2==0:
      return 0
  sumxy = 0
  for i in text1:
        sumxy += text1[i]*text2[i]
  return sumxy/(mod1*mod2)

def comparetexts(input_text,allDocuments):
    documents_compared={} #dict que guarda todos los documentos vectorizados en base al texto entrada
    #print("allDocuments: ",allDocuments)
    for doc in allDocuments:
        document=allDocuments[doc] #accedo al dict del documento 
        #print("documento: ",type(document))
        doc_vector={}
        for word in input_text: #verifico cada palabra del texto entrada
            #print(type(input_text))
            #print("tipo palabra", type(word))
            if word in document:
                 doc_vector[word]=document[word] #si se encuentra la palabra se toma su tf
            else:
                 doc_vector[word]=0.0 #sino, es cero
        documents_compared[doc]=doc_vector #agregar el vector al diccionario
        #print("quiero ver algo",doc_vector)
    return documents_compared
