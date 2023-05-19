def quickSort(lista):
    if len(lista) == 1 or len(lista) == 0:
        return lista
    else:
        pivot = lista[0]
        print(pivot)
        i = 0
        for j in range(len(lista)-1):
            if lista[j+1] < pivot:
                lista[j+1],lista[i+1] = lista[i+1], lista[j+1]
                i += 1
                print(lista)
        lista[0],lista[i] = lista[i],lista[0]
        primera = quickSort(lista[:i])
        segunda = quickSort(lista[i+1:])
        primera.append(lista[i])
        print(primera + segunda)
    return (primera + segunda)
