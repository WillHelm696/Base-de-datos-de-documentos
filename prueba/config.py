import os
def laod_file(ruta):
    Arr = os.listdir(ruta)
    print(Arr)
    return Arr

def sheatch_text(text):
    ruta= '/home/estudiante/Escritorio/Base-de-datos-de-documentos/prueba/archivos'
    Arr = laod_file(ruta)
    for archivo_input in Arr:
        archivo_input=os.path.join(ruta,archivo_input)
        with open(archivo_input,'r') as archivo:
            print(archivo.name)
            cont=0
            for linea in archivo:
                if text in linea:
                    cont+=1
                    print(linea.index(text))
                    print(linea.strip())
            if cont == 0:
                print("document not found")
        archivo.close()
        print("------------------------------------------------------------------------------------")
