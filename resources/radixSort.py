def mayor(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

def largo(num):
    if num == 0:
        return 1
    i = 0
    while num != 0:
        i += 1
        num = num//10
    return i

# **********************************************************
def radixSort(lista):
    if type(lista) == list:
        maxValor = mayor(lista)
        largoMax = largo(maxValor)
        i = 0
        while i < largoMax:
            l0 = []
            l1 = []
            l2 = []
            l3 = []
            l4 = []
            l5 = []
            l6 = []
            l7 = []
            l8 = []
            l9 = []
            for num in lista:
                temp = num//10**i%10
                if temp == 0:
                    l0 += [num]
                elif temp == 1:
                    l1 += [num]
                elif temp == 2:
                    l2 += [num]
                elif temp == 3:
                    l3 += [num]
                elif temp == 4:
                    l4 += [num]
                elif temp == 5:
                    l5 += [num]
                elif temp == 6:
                    l6 += [num]
                elif temp == 7:
                    l7 += [num]
                elif temp == 8:
                    l8 += [num]
                elif temp == 9:
                    l9 += [num]
            lista = l0 + l1 + l2 + l3 + l4 + l5+l6+l7+l8+l9
            i+=1
            print(lista)
            print("Lista 0: ", l0)
            print("Lista 1: ", l1)
            print("Lista 2: ", l2)
            print("Lista 3: ", l3)
            print("Lista 4: ", l4)
            print("Lista 5: ", l5)
            print("Lista 6: ", l6)
            print("Lista 7: ", l7)
            print("Lista 8: ", l8)
            print("Lista 9: ", l9)


        #print(lista) 
        return lista
