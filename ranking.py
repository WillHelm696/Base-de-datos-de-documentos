from similitud_coseno import *

#devuelve lista de (similitud_coseno, nombre del archivo, ruta y espacio para guardar texto)
def ranking(input_text,docs,rutas):
    docs=comparetexts(input_text,docs)
    ranked_docs=[]
    for item in docs:
        if item in rutas:
            r=(cosine_similarity(input_text,docs[item]),item,rutas[item],"agregar_texto")
        else:
            #se elimina mas adelante de la lista el elemento que no tiene ruta 
            r=(cosine_similarity(input_text,docs[item]),item,"sin ruta","texto_profe") 
        ranked_docs.append(r)
    ranked_docs = sorted(ranked_docs, key=lambda x: x[0], reverse=True) #ordena la lista de mayor a menor segun similitud
    return ranked_docs