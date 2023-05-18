def insertionSort(lista):
    for i in range (1,len(lista)):
        v=lista[i]
        j=i-1
        while j>=0 and lista[j]>v:
            lista[j+1]=lista[j]
            j=j-1
            print(lista)
        lista[j+1]=v
        print(lista)
    return lista
