# -*- coding: utf-8 -*-
"""Problema 3 - Divide y Vencerás


Aplicando la **estrategia de divide y vencerás**, implementa una función **recursiva** que reciba una lista de enteros, A, y un número entero, x,  
y devuelva una lista con los posiciones (índices) de x en la lista A. 
Si x no existe en la lista, la función debe devolver una lista vacía. 

Reglas:
- Recuerda que tu función debe ser recursiva y seguir el enfoque de divide y vencerás. Enfoques no recursivos y no basados en este enfoque no serán evaluados.
- Tu función no puede usar bucles ni listas auxiliares (de ningún tipo). 
- Tampoco puedes usar la funcion index de las listas de Python. 
- A no puede ser modificado (es decir, no puedes añadir o eliminar elementos de A)
"""

def getIndices(data,x):
    if data == None or len(data) == 0:
        return []
    if x not in data:
        return []
    listaIndices = []
    return _getIndices(data, x, 0, len(data) - 1, listaIndices)

def _getIndices(data, x, start, end, listaIndices):
    if start <= end:
        mid = (start + end) // 2
        if data[mid] == x:
            listaIndices.append(mid)
        _getIndices(data, x, start, mid - 1, listaIndices)
        _getIndices(data, x, mid + 1, end, listaIndices)
    listaIndices.sort()
    return listaIndices


"""A=[5,0,5,1,2,5,3,5]
x=5
expected=[]
for i,e in enumerate(A):
  if e==x:
    expected.append(i)

print(expected)

#expected=[0, 2, 5, 7]
result=getIndices(A,x)
print(result)"""

"""
import random
data=[]
for i in range(10):
  data.append(random.randint(0,5))

x=3
print('data:',data)
print('x:',x)


print(getIndices(data,x))
"""

import unittest


class Test(unittest.TestCase):

    #variable estática para almacenar la nota
    mark=0
    
    def setUp(self):
      self.x=5
      self.y=8
      self.z=1
      self.input=[5,0,5,1,2,5,5,5,0]

    def test1_getIndices(self):
      print('Caso 1: data es [] (nota: 0.5)')
      print('input:',[],'value:',self.x)
      self.assertEqual(getIndices([],self.x), [], 'FAIL: debería ser []')
      print('\t\t mark += 5')
      Test.mark+=5

    def test2_getIndices(self):
      print('...Caso 2: x no existe en data (nota: 0.5)')
      print('input:',self.input,'value:',self.y)
      self.assertEqual(getIndices(self.input,self.y), [], 'FAIL: debería ser []')
      print('\t\t mark += 5')
      Test.mark+=5

    def test3_getIndices(self):
      print('...Caso 3: x existe sólo una vez\n.')
      result=getIndices(self.input,self.z)
      expected=[self.input.index(self.z)]
      print('input:',self.input,'value:',self.z)
      print('result:',result)
      print('expected:',expected)
      self.assertListEqual(result,expected, 'FAIL: debería ser []')
      print('\t\t mark += 5')
      Test.mark+=5

    def test4_getIndices(self):
      print('...Caso 4: x existe varias veces\n.')
      result=getIndices(self.input,self.x)
      expected=[0, 2, 5, 6,7]

      print('input:',self.input,'value:',self.x)
      print('result:',result)
      print('expected:',expected)

      self.assertListEqual(result,expected, 'FAIL: debería ser [0, 2, 5, 6, 7]')
      print('\t\t mark += 5')
      Test.mark+=5

    def test_printNota(self):
      print('\n\n*************************')
      print("\n\t Provisional mark:  ",Test.mark)  
      print('*************************')


#Comentar para usarlo en spyder
#unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Descomenar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()
