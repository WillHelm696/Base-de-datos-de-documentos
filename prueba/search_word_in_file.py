def sheatch_text(text , archivo_input):
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