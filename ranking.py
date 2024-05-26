from similitud_coseno import *

def ranking(input_text,docs,rutas):
    docs=comparetexts(input_text,docs)
    #print("adentro de ranking")
    #print("docuemntos: ",type(docs),docs.keys(),docs)
    ranked_docs=[]
    for item in docs:
        #print("en el for: ", item)
        if item in rutas:
            r=(cosine_similarity(input_text,docs[item]),item,rutas[item],"agregar_texto")
        else:
            r=(cosine_similarity(input_text,docs[item]),item,"sin ruta","texto_profe")
            
        ranked_docs.append(r)
        
        #print(i," ",docs[i])
    #print(ranked_docs)
    ranked_docs = sorted(ranked_docs, key=lambda x: x[0], reverse=True)
    if len(ranked_docs) > 10:
        ranked_docs = ranked_docs[:10]
    return ranked_docs