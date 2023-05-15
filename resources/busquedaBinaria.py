def BusquedaBinaria(lista,num):
    if isinstance(lista,list) and isinstance(num,int):
        primero=0
        ultimo=len(lista)-1
        encontrado=False
        while primero<=ultimo and not encontrado:
            
            puntomedio=(primero+ultimo)//2
            if lista[puntomedio]==num:
                encontrado=True
            else:
                if num<lista[puntomedio]:
                    ultimo=puntomedio-1
                else:
                    primero=puntomedio+1
        print(encontrado)
                
    else:
        print ("Parametro incorrecto")
