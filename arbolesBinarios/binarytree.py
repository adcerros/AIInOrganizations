# -*- coding: utf-8 -*-
import queue #it is Python module to implement queues
#from queue import SQueue

class Node:
  def __init__(self,elem,left=None,right=None,parent=None):
    self.elem=elem
    self.left=left
    self.right=right
    self.parent=parent

  def compararNodos(self, nodo1, nodo2):
    return self._compararNodos(nodo1.parent, nodo2.parent)

  def _compararNodos(self, nodo1, nodo2):
    if nodo1 is None and nodo2 is None:
      return True
    if nodo1 is not None and nodo2 is None or nodo1 is None and nodo2 is not None:
      return False
    if nodo1.elem != nodo2.elem:
      return False
    else:
      return self._compararNodos(nodo1.right, nodo2.right) and self._compararNodos(nodo1.left, nodo2.left)

  def inorderToList(self,node):
    lista =[]
    self._inorderToList(node,lista)
    return lista

  def _inorderToList(self,node,lista):
    if node!=None:
      self._inorderToList(node.left,lista)
      lista.append(node.elem)
      self._inorderToList(node.right,lista)

class BinaryTree:
  
  def __init__(self):
    self.root=None

  def size(self):
    """Returns the number of nodes"""
    return self._size(self.root)

  def _size(self,node):
    "función recursiva de vuelve el tamaño de node"
    if node==None:
      return 0
      
    return 1 + self._size(node.left) + self._size(node.right)

  def height(self):
    """Returns the height of the tree"""
    return self._height(self.root)
  
  def _height(self,node):
    "función recursiva que devuelva la altura del nodo"
    if node==None:
      return -1

    return 1 + max(self._height(node.left),self._height(node.right))

  
  def depth(self,node):
    if node==None:
      return 0

    if node.parent==None: 
      #node==self.root
      return 0
    
    return 1 + self.depth(node.parent)

  def preorder(self):
    self._preorder(self.root)
    
  def _preorder(self,node):
    if node!=None:
      print(node.elem)
      self._preorder(node.left)
      self._preorder(node.right)

      
  def postorder(self):
    self._postorder(self.root)
    
  def _postorder(self,node):
    if node!=None:
      self._postorder(node.left)
      self._postorder(node.right)
      print(node.elem)
      
  def inorder(self):
    self._inorder(self.root)

  def _inorder(self,node):
    if node!=None:
      self._inorder(node.left)
      print(node.elem)
      self._inorder(node.right)

  def inorderToList(self):
    lista =[]
    self._inorderToList(self.root,lista)
    return lista

  def _inorderToList(self,node,lista):
    if node!=None:
      self._inorderToList(node.left,lista)
      lista.append(node.elem)
      self._inorderToList(node.right,lista)

  #Devuelve una lista con los elemetos comprendidos entre un rango (si incluir los extremos) en orden ascendente
  def inorderInRangeToList(self,min,max):
    lista =[]
    self._inorderInRangeToList(self.root,lista, min, max)
    return lista

  def _inorderInRangeToList(self,node,lista,min,max):
    if node!=None:
      self._inorderInRangeToList(node.left,lista,min,max)
      if node.elem > min and node.elem < max:
        lista.append(node.elem)
      self._inorderInRangeToList(node.right,lista,min,max)

  #Devuelve la suma de los elementos del arbol
  def inorderSuma(self):
    suma = 0
    return self._inorderSuma(self.root,suma)

  def _inorderSuma(self,node,suma):
    if node!=None:
      return suma + self._inorderSuma(node.left, suma) + node.elem + self._inorderSuma(node.right, suma)
    else:
      return 0

  def inorderAbueloMultiploDeX(self,x):
    self._inorderAbueloMultiploDeX(self.root,x)

  def _inorderAbueloMultiploDeX(self,node,x):
    if node!=None:
      self._inorderAbueloMultiploDeX(node.left,x)
      if node.parent != None:
        if node.parent.parent != None:
          if node.parent.parent.elem % x == 0:
            print(node.elem)
      self._inorderAbueloMultiploDeX(node.right,x)

  # Los metodos double order visitan  raiz- subarbol izq en double order - raiz - subarbol derecho en double order ////////////////////////////////
  def doubleOrder(self):
    self._doubleOrder(self.root)

  def _doubleOrder(self,node):
    if node!=None:
      print(node.elem)
      self._doubleOrder(node.left)
      print(node.elem)
      self._doubleOrder(node.right)

  def doubleOrderToList(self):
    lista =[]
    self._doubleOrderList(self.root,lista)
    return lista

  def _doubleOrderList(self,node,lista):
    if node!=None:
      lista.append(node.elem)
      self._doubleOrderList(node.left, lista)
      lista.append(node.elem)
      self._doubleOrderList(node.right, lista)
     
  def levelorder(self):
    if self.root==None:
      print('tree is empty')
      return
    
    q=queue.Queue()
    q.put(self.root) #enqueue: we save the root
    
    while q.empty()==False:
      current=q.get() #dequeue
      print(current.elem)
      if current.left!=None:
        q.put(current.left)
      if current.right!=None:
        q.put(current.right)


