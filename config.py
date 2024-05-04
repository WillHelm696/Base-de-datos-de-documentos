import os
# Guarda en una lista las rutas de los archivos 
def laod_file(ruta):
    lista = os.listdir(ruta)
    archivos = []
    for item in lista :
        contenido = os.path.join(ruta,item)
        if os.path.isfile(contenido):
            archivos.append(contenido)
        elif os.path.isdir(contenido):
            #Si hay una carpeta revisa el contenido y lo añade a la lista
            archivos += laod_file(contenido)
    return archivos

def sheatch_text(text,lista):
    #Recore la lista con la direcion de los archivos
    for item in lista:
        print("------------------------------------------------------------------------------------")
        with open(item,'r') as archivo:
            print(archivo.name)
            cont=0
            #document_bd() 
            for linea in archivo:
                if text in linea:
                    cont+=1
                    print(linea.index(text))
                    print(linea.strip())
            if cont == 0:
                print("document not found")
        archivo.close()

def document_bd(document):
    #Implemententar una base de datos con un documento
    return