def bubbleSort(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista)-i-1):
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
            print(lista)
        print(lista)
    print(lista)
    return lista
