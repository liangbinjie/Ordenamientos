def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Dividir el arreglo en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursivamente aplicar Merge Sort en ambas mitades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combinar las dos mitades ordenadas
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Comparar los elementos de las dos mitades y añadirlos al arreglo combinado
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Añadir los elementos restantes de la mitad izquierda (si los hay)
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Añadir los elementos restantes de la mitad derecha (si los hay)
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    print(merged)
    return merged