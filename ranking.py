from similitud_coseno import *
"""Hacer acá print de resultados como funcion y llamarlo desde ranking"""

#Recibe el texto ingresado por el profesor, la base de datos de los documentos con sus TF_IDF y las rutas de cada archivo
def ranking(input_text,docs,rutas):
    docsInput_text=comparetexts(input_text,docs)
    ranked_docs=[]
    for item in docs:
        if item in rutas:
            r=(cosine_similarity(docs[item],docsInput_text[item]),item,rutas[item],"agregar_texto")
        ranked_docs.append(r)
    ranked_docs = sorted(ranked_docs, key=lambda x: x[0], reverse=True) #ordena la lista de mayor a menor segun similitud
    #devuelve lista de (similitud_coseno, nombre del archivo, ruta y espacio para guardar texto)
    return ranked_docs