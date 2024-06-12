from similitud_coseno import *

#Recibe el texto ingresado por el profesor, la base de datos de los documentos con sus TF_IDF y las rutas de cada archivo
def ranking(input_text,docs,rutas):
    docsInput_text=comparetexts(input_text,docs)
    ranked_docs=[]
    for item in docs:
        if item in rutas:
            r=(cosine_similarity(docs[item],docsInput_text[item]),item,rutas[item])
        ranked_docs.append(r)
    ranked_docs = sorted(ranked_docs, key=lambda x: x[0], reverse=True) #ordena la lista de mayor a menor segun similitud
    print(" ")
    if ranked_docs[0][0]==0:
        print("document not found")
        return
    print("Ranking de documentos:")
    for i in range(0,10):
        print(i+1," ", ranked_docs[i][1])
        print(" ")
    print(" ")
    return 