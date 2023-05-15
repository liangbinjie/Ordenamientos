def shakeSort(lista):
    for i in range(len(lista)-1, 0, -1):
        is_swapped = False
        
        for j in range(i, 0, -1):
            if lista[j] < lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
                is_swapped = True

        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                is_swapped = True
        
        if not is_swapped:
            return lista