from bubbleSort import *
from busquedaBinaria import *
from insertionSort import *
from busquedaSecuencial import *
from mergeSort import *
from quickSort import *
from radixSort import *
from selectionSort import *
from shakeSort import *
from shellSort import *


def menu():
    running = True
    while running:
        print("***Ordenamientos***")
        print("Ingrese el ordenamiento que desea probar")
        print("[1] Burbuja")
        print("[2] Insercion")
        print("[3] QuickSort")
        print("[4] Merge")
        print("[5] Shell")
        print("[6] Radix")
        print("[7] Seleccion")
        print("[8] Shake")
        print("[9] Busqueda Binaria")
        print("[10] Busqueda Secuencial")
        opcion = input("> ")
        lista = input("Ingrese los elementos de la lista separados por un espacio: ").split()
        for i in range(len(lista)):
            lista[i] = int(lista[i])

        if opcion == "1":
            bubbleSort(lista)
        elif opcion == "2":
            insertionSort(lista)
        elif opcion == "3":
            quickSort(lista)
        elif opcion == "4":
            merge_sort(lista)
        elif opcion == "5":
            ordenShell(lista)
        elif opcion == "6":
            radixSort(lista)
        elif opcion == "7":
            selectionSort(lista)
        elif opcion == "8":
            shakeSort(lista)
        elif opcion == "9":
            num = int(input("Ingrese el numero a buscar: "))
            BusquedaBinaria(lista, num)
        elif opcion == "10":
            num = int(input("Ingrese el numero a buscar"))
            Busquedasecuencial(lista, num)
        else:
            print("Opcion incorrecta")

if __name__ == '__main__':
    menu()
            
        
