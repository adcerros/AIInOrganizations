import random

# METODOS DE POSICIONES Y NUMERICOS ////////////////////////////////////////////////////////////////////////////////////////////

#Retorna el mayor de una lista de enteros
def numeroMayor(lista):
    if lista == None or len(lista) == 0:
        return -1
    else:
        return _numeroMayor(lista,0,len(lista)-1)

def _numeroMayor(lista, start, end):
    if start == end:
        return lista[start]
    else:
        mid=(start+end)//2
        num1 = _numeroMayor(lista,start,mid)
        num2 = _numeroMayor(lista,mid+1,end)
        return max(num1,num2)

#Retorna el menor de una lista de enteros
def numeroMenor(lista):
    if lista == None or len(lista) == 0:
        return -1
    else:
        return _numeroMenor(lista,0,len(lista)-1)

def _numeroMenor(lista, start, end):
    if start == end:
        return lista[start]
    else:
        mid=(start+end)//2
        num1 = _numeroMenor(lista,start,mid)
        num2 = _numeroMenor(lista,mid+1,end)
        return min(num1,num2)

#Retorna el numero de veces que parece un elemento en la lista funciona tambien para strings
def numeroDeVeces(lista,elem):
    if lista == None or len(lista) == 0:
        return 0
    else:
        return _numeroDeVeces(lista, elem, 0, len(lista)-1)

def _numeroDeVeces(lista, elem, start, end):
    if start == end:
        if lista[start] == elem:
            return 1
        else:
            return 0
    else:
        mid=(start+end)//2
        return _numeroDeVeces(lista, elem, start, mid) + _numeroDeVeces(lista, elem, mid+1, end)

#Suma los elementos de la lista
def suma(lista):
    if lista == None or len(lista) == 0:
        return 0
    else:
        return _suma(lista, 0, len(lista)-1)

def _suma(lista, start, end):
    if start == end:
        return lista[start]
    else:
        mid=(start+end)//2
        return _suma(lista, start, mid) + _suma(lista, mid+1, end)

#Devuelve la media de los elementos de la lista
def media(lista):
    if lista == None or len(lista) == 0:
        return 0
    else:
        return _media(lista, 0, len(lista)-1) / len(lista)

def _media(lista, start, end):
    if start == end:
        return lista[start]
    else:
        mid=(start+end)//2
        return _media(lista, start, mid) + _media(lista, mid+1, end)

#Retorna el index de un elemento en la lista SI ESTA ORDENADA funciona tambien para strings
def index(lista, elem):
    if lista == None or len(lista) == 0:
        return -1

    return _index(lista, elem, 0, len(lista) - 1)

def _index(A, elem, start, end):
    if start <= end:
        mid = (start + end) // 2
        if lista[mid] == elem:
            return mid
        if elem < lista[mid]:
            return _index(A, elem, start, mid - 1)
        return _index(A, elem, mid + 1, end)
    return -1

def invertirLista(lista):
    listaAux = []
    if lista == None or len(lista) == 0:
        return listaAux
    else:
        _invertirLista(lista,0,len(lista)-1, listaAux)
    return listaAux

def _invertirLista(lista, start, end,listaAux):
    if start == end:
        listaAux.append(lista[start])
    else:
        mid=(start+end)//2
        _invertirLista(lista,mid+1,end, listaAux)
        _invertirLista(lista,start,mid, listaAux)

#Suma los elementos multiplos de 5 de la lista
def multiplos5(lista):
    if lista == None or len(lista) == 0:
        return 0
    else:
        return _multiplos5(lista, 0, len(lista)-1)

def _multiplos5(lista, start, end):
    if start == end:
        if lista[start] % 5 == 0:
            return lista[start]
        else:
            return 0
    else:
        mid=(start+end)//2
        return _multiplos5(lista, start, mid) + _multiplos5(lista, mid+1, end)

# METODOS PARA PARES E IMPARES ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Retorna el par mas pequeño de una lista de enteros
def parMasPequeño(lista):
    if lista == None or len(lista) == 0:
        return None
    else:
        return _parMasPequeño(lista,0,len(lista)-1)

def _parMasPequeño(lista, start, end):
    if start == end:
        if lista[start] % 2 == 0:
            return lista[start]
        else:
            return None
    else:
        mid=(start+end)//2
        num1 = _parMasPequeño(lista,start,mid)
        num2 = _parMasPequeño(lista,mid+1,end)
        if num1 == None:
            return num2
        if num2 == None:
            return num1
        return min(num1,num2)

#Retorna el par mas grande de una lista de enteros
def parMasGrande(lista):
    if lista == None or len(lista) == 0:
        return None
    else:
        return _parMasGrande(lista,0,len(lista)-1)

def _parMasGrande(lista, start, end):
    if start == end:
        if lista[start] % 2 == 0:
            return lista[start]
        else:
            return None
    else:
        mid=(start+end)//2
        num1 = _parMasGrande(lista,start,mid)
        num2 = _parMasGrande(lista,mid+1,end)
        if num1 == None:
            return num2
        if num2 == None:
            return num1
        return max(num1,num2)

#Retorna el impar mas pequeño de una lista de enteros
def imparMasPequeño(lista):
    if lista == None or len(lista) == 0:
        return None
    else:
        return _imparMasPequeño(lista,0,len(lista)-1)

def _imparMasPequeño(lista, start, end):
    if start == end:
        if lista[start] % 2 != 0:
            return lista[start]
        else:
            return None
    else:
        mid=(start+end)//2
        num1 = _imparMasPequeño(lista,start,mid)
        num2 = _imparMasPequeño(lista,mid+1,end)
        if num1 == None:
            return num2
        if num2 == None:
            return num1
        return min(num1,num2)

#Retorna el impar mas grande de una lista de enteros
def imparMasGrande(lista):
    if lista == None or len(lista) == 0:
        return None
    else:
        return _imparMasGrande(lista,0,len(lista)-1)

def _imparMasGrande(lista, start, end):
    if start == end:
        if lista[start] % 2 != 0:
            return lista[start]
        else:
            return None
    else:
        mid=(start+end)//2
        num1 = _imparMasGrande(lista,start,mid)
        num2 = _imparMasGrande(lista,mid+1,end)
        if num1 == None:
            return num2
        if num2 == None:
            return num1
        return max(num1,num2)

# Devuelve el par y el impar mas pequeño de la lista
def parEImparMasPequeño(lista):
    par = parMasPequeño(lista)
    impar = imparMasPequeño(lista)
    if par == None or impar == None:
        return None
    else:
        return par, impar

# Devuelve el par y el impar mas grande de la lista
def parEImparMasGrande(lista):
    par = parMasGrande(lista)
    impar = imparMasGrande(lista)
    if par == None or impar == None:
        return None
    else:
        return par, impar

# METODOS PARA NUMEROS Y LETRAS MEZCLADOS ////////////////////////////////////////////////////////////////////////////////////////////

def masLetrasONumeros(lista):
    if lista == None or len(lista) == 0:
        return None
    else:
        listaLetras = []
        listaNumeros = []
        resultado = _masLetrasONumeros(lista, 0, len(lista) - 1, listaLetras, listaNumeros)
        if resultado == 0:
            print("Mas numeros")
        if resultado == 1:
            print("Mas letras")
        if resultado == 2:
            print("Empate")


def _masLetrasONumeros(lista, start, end, listaLetras, listaNumeros):
    if start == end:
        if type(lista[start]) == int:
            listaNumeros.append(lista[start])
        if type(lista[start]) == str:
            listaLetras.append(lista[start])
    else:
        mid = (start + end) // 2
        _masLetrasONumeros(lista, start, mid, listaLetras, listaNumeros)
        _masLetrasONumeros(lista, mid + 1, end, listaLetras, listaNumeros)
    if len(listaNumeros) > len(listaLetras):
        return 0
    if len(listaNumeros) < len(listaLetras):
        return 1
    else:
        return 2

# METODOS PARA CADENAS DE TEXTO ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Retorna la cadena mas grande de la lista
def cadenaMasGrande(lista):
    if lista == None or len(lista) == 0:
        return -1
    else:
        return _cadenaMasGrande(lista,0,len(lista)-1)

def _cadenaMasGrande(lista, start, end):
    if start == end:
        return lista[start]
    else:
        mid=(start+end)//2
        cadena1 = _cadenaMasGrande(lista,start,mid)
        cadena2 = _cadenaMasGrande(lista,mid+1,end)
        if len(cadena1) > len(cadena2):
            return cadena1
        if len(cadena1) < len(cadena2):
            return cadena2
        if len(cadena1) == len(cadena2):
            return cadena2

#Retorna la cadena mas pequeña de la lista
def cadenaMasPequeña(lista):
    if lista == None or len(lista) == 0:
        return -1
    else:
        return _cadenaMasPequeña(lista,0,len(lista)-1)

def _cadenaMasPequeña(lista, start, end):
    if start == end:
        return lista[start]
    else:
        mid=(start+end)//2
        cadena1 = _cadenaMasPequeña(lista,start,mid)
        cadena2 = _cadenaMasPequeña(lista,mid+1,end)
        if len(cadena1) > len(cadena2):
            return cadena2
        if len(cadena1) < len(cadena2):
            return cadena1
        if len(cadena1) == len(cadena2):
            return cadena1

#Retorna las cadenas con longitud menor de x
def cadenasMenorQue(lista,x):
    lista2 = []
    if lista == None or len(lista) == 0:
        return lista2
    else:
        _cadenasMenorQue(lista,0,len(lista)-1, x ,lista2)
    return lista2

def _cadenasMenorQue(lista, start, end, x, lista2):
    if start == end:
        palabra = lista[start]
        if len(palabra) <= x:
            lista2.append(palabra)
    else:
        mid=(start+end)//2
        _cadenasMenorQue(lista, start, mid, x, lista2)
        _cadenasMenorQue(lista, mid+1, end, x, lista2)

#Retorna las cadenas con longitud mayor de x
def cadenasMayorQue(lista,x):
    lista2 = []
    if lista == None or len(lista) == 0:
        return lista2
    else:
        _cadenasMayorQue(lista,0,len(lista)-1, x ,lista2)
    return lista2

def _cadenasMayorQue(lista, start, end, x, lista2):
    if start == end:
        palabra = lista[start]
        if len(palabra) >= x:
            lista2.append(palabra)
    else:
        mid=(start+end)//2
        _cadenasMayorQue(lista, start, mid, x, lista2)
        _cadenasMayorQue(lista, mid+1, end, x, lista2)

# Retorna el numero de veces que aparece un char en un string
def count(string, char):
     if string is None or len(string)==0:
        return 0
     mid= len(string) // 2
     result=0
     if string[mid]==char:
         result +=1
         count1=count(string[0:mid], char)
         count2=count(string[mid + 1:], char)
         return result + count1+count2


lista = ["hla","uno","dos","esparadrapo","chubascos","trs","agu"]
print(lista)
print(cadenasMenorQue(lista,4))
print(cadenasMayorQue(lista,4))