def Busquedasecuencial(lista,num):
    if type(lista)==list and type(num)==int:
        posicion=0
        encontrado=False
        while posicion < len(lista) and not encontrado:
            print(posicion)
            if lista[posicion]==num:        
                encontrado=True 

            else:
                posicion=posicion+1
        print(encontrado)
    else:
        print("Parametro incorrecto")
