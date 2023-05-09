def bubbleSort(lista):
    for i in range(1, len(lista)):
        for j in range(0, len(lista)-i):
            if lista[j] > lista[j+1]:
                k = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = k
    #print(lista)
    return lista
