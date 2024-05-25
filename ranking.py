from similitud_coseno import *

def ranking(input_text,docs):
    docs=comparetexts(input_text,docs)
    ranked_docs=[]
    for i in range(0,len(docs)):
        r=(cosine_similarity(input_text,docs[i]),"agregar_nombre","agregar_ruta","agregar_texto")
        ranked_docs.append(r)
        #print(i," ",docs[i])
    #print(ranked_docs)
    ranked_docs = sorted(ranked_docs, key=lambda x: x[0], reverse=True)
    if len(ranked_docs) > 10:
        ranked_docs = ranked_docs[:10]
    return ranked_docs