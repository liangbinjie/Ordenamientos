def selectionSort(lista):
    for i in range(0,len(lista)-1):
        minimo=i
        for j in range(i+1,len(lista)):
            if lista[minimo]>lista[j]:
                minimo=j#2 2 4
             aux=lista[minimo]
        lista[minimo]=lista[i]
        lista[i]=aux
    #print(lista)
    return lista
