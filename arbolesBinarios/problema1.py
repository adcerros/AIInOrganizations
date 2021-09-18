# -*- coding: utf-8 -*-
"""Problema1-checkcousins.ipynb

# PROBLEMA - ÁRBOLES (20 puntos)

Sea MyBST la clase que implementa un árbol binario de búsqueda en Python (en realidad es una versión reducida que sólo incluye los métodos necesarios para este problema).

Dos nodos son primos si están en el mismo nivel (tienen la misma profundidad) y además sus padres son hermanos.

En la clase BST, completa el método checkCousins(a,b) que tomas dos elementos  y devuelve True si sus nodos son primos, y False en otro caso.
"""

class Node: 
    def __init__(self,elem,left=None,right=None,parent=None):
        self.elem=elem
        self.left=left
        self.right=right
        self.parent=parent
        
    
class MyBST:
    
    def __init__(self):
        self.root=None
    
    def depth(self,node):
        """returns the depth of node"""
        if node==None or node.parent==None:
            return 0
        
        return 1 + self.depth(node.parent)

    def find(self,x):
        """Returns the whose element is x. 
        None if x does not exist into the tree"""
        return self._find(self.root,x)

    def _find(self,node,x):
        if node==None:
            return None
        if node.elem==x:
            return node
        if x<node.elem:
            return self._find(node.left,x)
        if x>node.elem:
            return self._find(node.right,x)
        
    def insert(self,x):
        """inserts a new node, with element x, into the tree"""
        if self.root==None:
            self.root=Node(x)
        else:
            self._insertNode(self.root,x)


    def _insertNode(self,node,x):
        if node.elem==x:
            #print('Error: la clave ya existe. No permitimos duplicados')
            return 
        if x<node.elem:

            if node.left==None:
                #ya he encontrado su sitio
                newNode=Node(x)
                newNode.parent=node
                node.left=newNode
            else:
                self._insertNode(node.left,x)

        else: #x>node.elem

            if node.right==None:
                #ya he encontrado la posición
                newNode=Node(x)
                newNode.parent=node
                node.right=newNode
            else:
                 self._insertNode(node.right,x)
        

    def draw(self):
      """Function to draw the tree"""
      self._draw('',self.root,False)
      print()
      
    def _draw(self,prefix, node, isLeft):
        if node !=None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + ("|-- ") + str(node.elem))
            self._draw(prefix + "     ", node.left, True)


    def checkCousins(self,x,y):
        if x == None or y == None:
            return False
        node1 = self.find(x)
        node2 = self.find(y)
        if node1 == None or node2 ==None:
            return False
        if node1.parent == None or node2.parent ==None:
            return False
        if node1.parent.parent == None or node2.parent.parent ==None:
            return False
        else:
            if node1.parent.parent.elem == node2.parent.parent.elem and self.depth(node1) == self.depth(node2):
                if node1.parent.elem == node2.parent.elem:
                    return False
                else:
                    return True
            else:
                return False

"""
import random
tree=MyBST()

values=[25,20,36,10,22,30,40,5,12,28,38,48]
tree=MyBST()
for x in values:
    tree.insert(x)


print('5 and 15 are cousins?:',tree.checkCousins(5,15)) #False, 15 does not exist
print('5 and 22 are cousins?:',tree.checkCousins(5,22)) #False, have diferent levels
print('5 and 22 are cousins?:',tree.checkCousins(5,22)) #False, have diferent levels
print('36 and 48 are cousins?:',tree.checkCousins(36,48)) #False, have diferent levels
print('5 and 12 are cousins?:',tree.checkCousins(5,12)) #False, are siblings
print('20 and 36 are cousins?:',tree.checkCousins(20,36)) #False, are siblings
print('10 and 22 are cousins?:',tree.checkCousins(10,22)) #False, are siblings
print('5 and 28 are cousins?:',tree.checkCousins(5,28)) #False, same level, their parents are not siblings
print('12 and 28 are cousins?:',tree.checkCousins(12,28)) #False, same level, their parents are not siblings
print('10 and 30 are cousins?:',tree.checkCousins(10,30)) #True, are cousins
print('10 and 40 are cousins?:',tree.checkCousins(10,30)) #True, are cousins
print('22 and 30 are cousins?:',tree.checkCousins(22,30)) #True, are cousins
print('22 and 40 are cousins?:',tree.checkCousins(22,40)) #True, are cousins
print('28 and 38 are cousins?:',tree.checkCousins(28,38)) #True, are cousins
print('28 and 48 are cousins?:',tree.checkCousins(28,48)) #True, are cousins

tree.draw()


"""

import unittest


class Test(unittest.TestCase):

    #provisional mark
    mark=0

    def setUp(self):
        values=[12, 16, 19, 20, 4, 14, 2, 18, 10, 8, 24, 6, 1, 13]
        self.bst=MyBST()
        for x in values:
            self.bst.insert(x)
        

        self.data=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        
        #self.bst.draw()
    
    def test7_printNota(self):
        print('\n\n*************************')
        print("\t Provisional mark:",Test.mark)  
        print('*************************')

    def test1_checkCousins(self):
        print('Caso 1: a does not in the tree, a=',self.data[0],', b=',self.data[1])
        self.assertEqual(self.bst.checkCousins(self.data[0],self.data[1]), False)
        print('\t\t mark += 1')
        Test.mark+=1

    def test2_checkCousins(self):
        print('Caso 2: b does not in the tree, a=',self.data[1],', b=',self.data[5])
        self.assertEqual(self.bst.checkCousins(self.data[0],self.data[1]), False)
        print('\t\t mark += 1')
        Test.mark+=1

    def test3_checkCousins(self):
        print('Caso 3: a y b have different depths, a=',self.data[1],', b=',self.data[4])
        self.assertEqual(self.bst.checkCousins(self.data[1],self.data[4]), False)
        print('\t\t mark += 3')
        Test.mark+=3

    def test4_checkCousins(self):
        print('Caso 4: a and b are siblings, a=',self.data[2],', b=',self.data[10])
        self.assertEqual(self.bst.checkCousins(self.data[2],self.data[10]), False)
        print('\t\t mark += 5')
        Test.mark+=5

    def test5_checkCousins(self):
        print('Caso 5: a and b are not cousing and not siblings, a=',self.data[8],', b=',self.data[13])
        self.assertEqual(self.bst.checkCousins(self.data[8],self.data[13]), False)
        print('\t\t mark += 5')
        Test.mark+=5
    
    def test6_checkCousins(self):
        print('Caso 6: a and b are  cousins a=',self.data[2],', b=',self.data[19])
        self.assertEqual(self.bst.checkCousins(self.data[2],self.data[19]), True)
        print('\t\t mark += 5')
        Test.mark+=5
        
    


#Comentar para usarlo en google colab
#unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Descomenar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()