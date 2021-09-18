from ExamenFinalEDA.arbolesBinarios.binarysearchtree import BinarySearchTree
from ExamenFinalEDA.myqueue import SQueue
from ExamenFinalEDA.arbolesBinarios.binarytree import Node


class BinarySearchTreeExamen(BinarySearchTree):

    # METODOS PARA NODOS ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # Crea un arbol perfectamente balanceado desde una lista (equilibrado en tamaño)
    def balanceadoDesdeLista(self, lista):
        if lista == None:
            return None
        if len(lista) == 1:
            self.root == lista[0]
        else:
             lista.sort()
             self._balanceadoDesdeLista(lista, 0, len(lista)-1)

    def _balanceadoDesdeLista(self, lista, start, end):
        if start > end:
            return
        else:
            mid = (start + end) // 2
            self.insert(lista[mid])
            self._balanceadoDesdeLista(lista, start, mid-1)
            self._balanceadoDesdeLista(lista, mid + 1, end)

    #Devuelve true si el arbol es bst y false si no cumple la definicion
    def isBst(self):
        if self.root == None:
            return True
        if self.root.elem == None:
            return True
        else:
            return self._isBstLeft(self.root.left) and self._isBstRight(self.root.right)

    def _isBstLeft(self,node):
        if node == None:
            return True
        if node.elem == None:
            return False
        else:
            if node.elem < node.parent.elem:
                return self._isBstLeft(node.left) and self._isBstRight(node.right)
            else:
                return False

    def _isBstRight(self,node):
        if node == None:
            return True
        else:
            if node.elem > node.parent.elem:
                return self._isBstLeft(node.left) and self._isBstRight(node.right)
            else:
                return False

    # Elimina y retorna el elemento con la key mas pequeña del arbol
    def removeMin(self):
        if self.root == None:
            return None
        if self.root.left == None:
            elem = self.root.elem
            if self.root.right != None:
                self.root = self.root.right
                return elem
        else:
            return self._removeMin(self.root.left)
    def _removeMin(self,node):
        if node.left == None:
            elem = node.elem
            if node.right != None:
                node.right.parent = node.parent
                node.parent.left = node.right
            else:
                node.parent.left = None
            return elem
        else:
             return self._removeMin(node.left)

    # Elimina y retorna el elemento con la key mas grande del arbol
    def removeMax(self):
        if self.root == None:
            return None
        if self.root.right == None:
            elem = self.root.elem
            if self.root.left != None:
                self.root = self.root.left
                return elem
        else:
            return self._removeMax(self.root.right)
    def _removeMax(self,node):
        if node.right == None:
            elem = node.elem
            if node.left != None:
                node.left.parent = node.parent
                node.parent.right = node.left
            else:
                node.parent.right = None
            return elem
        else:
             return self._removeMax(node.right)

    #Devuelve el arbol en espejo
    def mirror(self):
        self._mirror(self.root)

    def _mirror(self, node):
        if node is None:
            return
        self._mirror(node.left)
        self._mirror(node.right)
        temp = node.left
        node.left = node.right
        node.right = temp

    #Imprime el subarbol del nodo por niveles
    def nodeSubtreeLevelOrder(self,node):
        if node != None:
            cola = SQueue()
            cola.enqueue(node)
            while cola.isEmpty()==False:
                current = cola.dequeue()
                print(current.elem)
                if current.left != None:
                    cola.enqueue(current.left)
                if current.right != None:
                    cola.enqueue(current.right)
        else:
            return

    #Devuelve una lista con todos los padres directos del nodo
    def returnParentsNode(self,node):
        lista = []
        return self._returnParentsNode(node,lista)

    def _returnParentsNode(self,node,lista):
        if node == None:
            return
        if node == self.root:
            return lista
        else:
            lista.append(node.parent.elem)
            return self._returnParentsNode(node.parent,lista)

    #Retorna el factor de equilibrio en tamaño de un nodo
    def fsize(self, node):
        if node is None:
            return 0
        return abs(self._size(node.left) - self._size(node.right))

    #Retorna el factor de equilibrio en altura de un nodo
    def fheight(self, node):
        if node is None:
            return 0
        return abs(self._height(node.left) - self._height(node.right))

    #Comprueba si el arbol esta equilibrado en tamaño
    def isSizeBalanced(self):
        return self._isSizeBalanced(self.root)

    def _isSizeBalanced(self, node):
        if node is None:
            return True
        if self.fsize(node) > 1:
            return False
        return self._isSizeBalanced(node.left) and self._isSizeBalanced(node.right)

    #Comprueba si el arbol esta equilibrado en altura
    def isAVL(self):
        return self._isAVL(self.root)

    def _isAVL(self, node):
        if node is None:
            return True
        if self.fheight(node) > 1:
            return False
        return self._isAVL(node.left) and self._isAVL(node.right)

    #Retorna el predecesor de un nodo
    def predecessor(self, node):
        if node is None:
            return None
        if node.left is None:
            return None
        predecessor = node.left
        while predecessor.right:
            predecessor = predecessor.right

        return predecessor

    # Retorna el sucesor de un nodo
    def successor(self, node):
        if node is None:
            return None
        if node.right is None:
            return None
        successor = node.right
        while successor.left:
            successor = successor.left
        return successor

    #Equilibra un arbol en amplitud
    def balance(self):
        if self.isSizeBalanced() == True:
            return
        self.balance_node(self.root)

    def balance_node(self, node):
        if node == None:
            return
        while self._size(node.left) - 1 > self._size(node.right):
            if node.right == None:
                newnode = Node(node.elem)
                newnode.parent = node
                node.right = newnode
            else:
                self._insertNode(node.right, node.elem)
            successor = node.left
            while successor.right != None:
                successor = successor.right
            x = self.find(successor.elem)
            self._borrar(x)
            node.elem = x.elem
            value = self.fsize(node)

        while self._size(node.left) < self._size(node.right) - 1:
            if node.left == None:
                newnode = Node(node.elem)
                newnode.parent = node
                node.left = newnode
            else:
                self._insertNode(node.left, node.elem)
            successor = node.right
            while successor.left != None:
                successor = successor.left
            x = self.find(successor.elem)
            self._removeNode(x)
            node.elem = x.elem
            value = self.fsize(node)
        if self.isSizeBalanced() != True and node != None:
            self.balance_node(node.right)
            self.balance_node(node.left)

    # METODOS PARA ELEM /////////////////////////////////////////////////////////////////////////////////////////////////////

    #Busca un nodo por su elem e imprime el subarbol del nodo por niveles
    def elemSubtreeLevelOrder(self,elem):
        node = self.searchNodeForElem(elem)
        if node != None:
            cola = SQueue()
            cola.enqueue(node)
            while cola.isEmpty()==False:
                current = cola.dequeue()
                print(current.elem)
                if current.left != None:
                    cola.enqueue(current.left)
                if current.right != None:
                    cola.enqueue(current.right)
        else:
            print("Elem is not on the tree")
            return

    #Busca un elem dentro del arbol y devuelve su nodo
    def searchNodeForElem(self,elem):
        return self._searchNodeForElem(self.root, elem)

    def _searchNodeForElem(self,node,elem):
        if node is None:
            return None
        if node.elem == elem:
            return node
        if elem < node.elem:
            return self._searchNodeForElem(node.left, elem)
        if elem > node.elem:
            return self._searchNodeForElem(node.right, elem)

    #Devuelve una lista con todos los padres directos del elem
    def returnParents(self,elem):
        node = self.searchNodeForElem(elem)
        if node == None:
            return None
        else:
            lista = []
            return self._returnParents(node,lista)

    def _returnParents(self,node,lista):
        if node == None:
            return
        if node == self.root:
            return lista
        else:
            lista.append(node.parent.elem)
            return self._returnParents(node.parent,lista)

    # Retorna el predecesor de un elem en el arbol
    def setPredecesorElem(self, elem):
        node = self.searchNodeForElem(elem)
        if node == None:
            return None
        if node.left == None:
            return node
        else:
            return self.setPredecesorElem(node.left.elem)

    # Retorna el sucesor de un elem en el arbol
    def setSucesorElem(self, elem):
        node = self.searchNodeForElem(elem)
        if node == None:
            return None
        if node.right == None:
            return node
        else:
            return self.setSucesorElem(node.right.elem)

    # Retorna el factor de equlibrio en TAMAÑO dado un elem
    def factorEquilibrioElem(self, elem):
        node = self.searchNodeForElem(elem)
        if node is None:
            return 0
        else:
            leftSize = self._size(node.left)
            rightSize = self._size(node.right)
            return abs(leftSize - rightSize)

# METODOS PARA COMPARAR ARBOLES

# Recibe dos arboles y devuelve una lista con sus elementos comunes
    def returnSimilar(self,arbol1,arbol2):
        listaComunes = []
        if arbol1 == None or arbol2 == None:
            return listaComunes
        else:
            listaArbol1 = arbol1.inorderToList()
            listaArbol2 = arbol2.inorderToList()
            i=0
            while i < len(listaArbol1):
                elem = listaArbol1[i]
                if elem in listaArbol2:
                    listaComunes.append(elem)
                i += 1
        return listaComunes

    def returnSimilarSinListas(self,arbol1,arbol2):
        listaComunes = []
        self._returnSimilarSinListas(arbol1.root,arbol2, listaComunes)
        return listaComunes

    def _returnSimilarSinListas(self, node, arbol2, listaComunes):
        if node is not None:
            self._returnSimilarSinListas(node.left, arbol2 ,listaComunes)
            if arbol2.find(node.elem) is not None:
                listaComunes.append(node.elem)
            self._returnSimilarSinListas(node.right, arbol2, listaComunes)

# Recibe dos arboles y devuelve true si son iguales
    def arbolesIguales(self,arbol1,arbol2):
        if arbol1 == None or arbol2 == None:
            return True
        else:
            listaArbol1 = arbol1.inorderToList()
            listaArbol2 = arbol2.inorderToList()
            if listaArbol1 == listaArbol2:
                return True
            else:
                return False

    def arbolesIgualesSinListas(self,arbol1,arbol2):
        return self._arbolesIgualesSinListas(arbol1.root, arbol2.root)

    def _arbolesIgualesSinListas(self,nodo1,nodo2):
        if nodo1 is None and nodo2 is None:
            return True
        if nodo1 is not None and nodo2 is None or nodo1 is None and nodo2 is not None:
            return False
        if nodo1.elem != nodo2.elem:
            return False
        else:
            return self._arbolesIgualesSinListas(nodo1.right, nodo2.right) and self._arbolesIgualesSinListas(nodo1.left, nodo2.left)


lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [2,5,9,10,22,32,43,54]
arbol = BinarySearchTreeExamen()
arbol.balanceadoDesdeLista(lista1)
arbol2 = BinarySearchTreeExamen()
arbol.insert(90)
arbol.insert(110)
arbol.insert(190)
arbol.insert(199)
print(arbol.isSizeBalanced())
arbol.draw()
arbol.balance()
arbol.draw()
print(arbol.isSizeBalanced())
arbol2.balanceadoDesdeLista(lista2)
print(arbol.returnSimilarSinListas(arbol,arbol2))

