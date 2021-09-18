import random
from ExamenesEDA.dlist import DList
from ExamenesEDA.slist_with_head_and_tail import SList
from ExamenesEDA.slist_only_head import SListH


def mergesort(lista):
    if lista == None or len(lista) <= 1:
        return lista
    if len(lista) > 1:
        mid = len(lista) // 2
        parte1 = lista[0:mid]
        parte2 = lista[mid:]
        sorted1 = mergesort(parte1)
        sorted2 = mergesort(parte2)
        return merge(sorted1, sorted2)

def merge(lista1, lista2):
    result = []
    i = 0
    j = 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
    while i < len(lista1):
        result.append(lista1[i])
        i += 1
    while j < len(lista2):
        result.append(lista2[j])
        j += 1
    return result

def mergesortDlist(lista):
    if lista == None or lista.size <= 1:
        return lista
    if lista.size > 1:
        mid = lista.size // 2
        lista1 = DList()
        lista2 = DList()
        i=0
        j= mid
        while i < mid:
            lista1.addLast(lista.getAt(i))
            i +=1
        while j < lista.size:
            lista2.addLast(lista.getAt(j))
            j += 1
        sorted1 = mergesortDlist(lista1)
        sorted2 = mergesortDlist(lista2)
        return mergeDlist(sorted1, sorted2)

def mergeDlist(lista1, lista2):
    result = DList()
    i = 0
    j = 0
    while i < lista1.size and j < lista2.size:
        if lista1.getAt(i) < lista2.getAt(j):
            result.addLast(lista1.getAt(i))
            i += 1
        else:
            result.addLast(lista2.getAt(j))
            j += 1
    while i < lista1.size:
        result.addLast(lista1.getAt(i))
        i += 1
    while j < lista2.size:
        result.addLast(lista2.getAt(j))
        j += 1
    return result

def mergesortDlistSinGetAt(list):
    if list.size <= 1:
        return list
    size = list.size
    mid = list.size//2
    lista1 = DList()
    lista2 = DList()
    i = 0
    j = mid
    while i < mid:
        lista1.addLast(list.removeFirst())
        i += 1
    while j < size:
        lista2.addLast(list.removeFirst())
        j += 1
    sorted1 = mergesortDlistSinGetAt(lista1)
    sorted2 = mergesortDlistSinGetAt(lista2)
    return mergeDlistSinGetAt(sorted1, sorted2)

def mergeDlistSinGetAt(lista1, lista2):
    result = DList()
    i = 0
    j = 0
    size1 = lista1.size
    size2 = lista2.size
    elem1 = lista1.removeFirst()
    elem2 = lista2.removeFirst()
    while i < size1 and j < size2:
        if elem1 < elem2:
            result.addLast(elem1)
            i += 1
            if i < size1:
                elem1 = lista1.removeFirst()
        else:
            result.addLast(elem2)
            j += 1
            if j < size2:
                elem2 = lista2.removeFirst()
    if i == size1:
        while elem2 is not None:
            result.addLast(elem2)
            if lista2.size > 0:
                elem2 = lista2.removeFirst()
            else:
                elem2 = None
    if j == size2:
        while elem1 is not None:
            result.addLast(elem1)
            if lista1.size > 0:
                elem1 = lista1.removeFirst()
            else:
                elem1 = None
    return result

# METODOS QUICKSORT /////////////////////////////////////////////////////////////////////////////

def quicksortMedio(lista):
    _quicksortMedio(lista, 0, len(lista) - 1)

def _quicksortMedio(lista, left, right):
    i = left
    j = right
    mid = (left + right) // 2
    p = lista[mid]
    while i <= j:
        while lista[i] < p:
            i += 1
        while lista[j] > p:
            j -= 1
        if i <= j:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
            j -= 1
    if left < j:
        _quicksortMedio(lista, left, j)
    if i < right:
        _quicksortMedio(lista, i, right)

def partitionIzquierda(lista):
    menor = []
    mayor = []
    pivot = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < pivot:
            menor.append(lista[i])
        else:
            mayor.append(lista[i])
    return (menor, pivot, mayor)

def quicksortIzquierda(lista):
    if len(lista) < 2:
        return lista
    menor, p, mayor = partitionIzquierda(lista)
    return quicksortIzquierda(menor) + [p] + quicksortIzquierda(mayor)

def partitionDerecha(lista):
    menor = []
    mayor = []
    pivot = lista[-1]

    for i in range(0, len(lista) - 1):
        if lista[i] < pivot:
            menor.append(lista[i])
        else:
            mayor.append(lista[i])

    return (menor, pivot, mayor)

def quicksortDerecha(lista):
    if len(lista) < 2:
        return lista
    menor, pivot, mayor = partitionDerecha(lista)
    return quicksortDerecha(menor) + [pivot] + quicksortDerecha(mayor)

def quicksortAleatorio(lista):
    _quicksortAleatorio(lista, 0, len(lista) - 1)

def _quicksortAleatorio(lista, left, right):
    i, j = left, right
    pivot = lista[random.randint(left, right)]
    while i <= j:
        while lista[i] < pivot:
            i += 1
        while lista[j] > pivot:
            j -= 1
        if i <= j:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
            j -= 1
    if left < j:
        _quicksortAleatorio(lista, left, j)
    if i < right:
        _quicksortAleatorio(lista, i, right)



lista = [5,4,7,10,9,17,15,12,90,104]
listaDoble = DList()
listaDoble.addLast(5)
listaDoble.addLast(4)
listaDoble.addLast(1)
listaDoble.addLast(19)
listaDoble.addLast(3)
listaDoble.addLast(8)
listaDoble.addLast(0)
listaDoble.addLast(11)
listaDoble.addLast(23)
listaDoble.addLast(17)
listaDoble.addLast(19)
listaDoble.addLast(19)
listaDoble.addLast(105)
print(listaDoble.size)
print(mergesortDlistSinGetAt(listaDoble))