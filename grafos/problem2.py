# -*- coding: utf-8 -*-
"""Problem2-undirectedDisjktra.ipynb

#Problem 2 - Grafos

Sea Graph la implementación de un grafo dirigido no ponderado. Implementa una funcion, minimumPath, que reciba dos vértices start y end, y devuelve la lista que represente el camino mínimo entre start y end. Si start o end no existen, la función devuelve la lista vacía []. 

"""

import sys
class Graph():
    def __init__(self,labels):
        """uses a dictionary to represent the graph"""
        self.labels = labels
        self.vertices={}
        for v in labels:
            self.vertices[v]=[]
       
    def addEdge(self, start, end):
        """adds an edge from start to end"""
        if start not in self.vertices.keys():
            return
        if end not in self.vertices.keys():
            return
        self.vertices[start].append(end)

   

    def minimumPath(self,start,end):
        visited = []
        if start == end :
            return visited
        if self.vertices[start] == None or self.vertices[end] == None:
            return visited
        listaVertices = self.labels
        while not len(listaVertices) == 0:
            current = listaVertices.pop(0)
            if current not in visited:
                visited.append(current)
                if current == end:
                    return visited
            j = 0
            while j < len(self.vertices[current]):
                if self.vertices[current][j] not in visited:
                    listaVertices.append(self.vertices[current][j])
                j += 1
        return visited


"""
labels=['A', 'B', 'C', 'D', 'E','F','G']    

g = Graph(labels)  
g.addEdge('A', 'B')
g.addEdge('B', 'C')
g.addEdge('B', 'D')
g.addEdge('B', 'E')
g.addEdge('C', 'E')
g.addEdge('D', 'E')
g.addEdge('E', 'F')
g.addEdge('G', 'D')

print('minimum paths from A:')

print(g.minimumPath('A','A')) #[]
print(g.minimumPath('A','B')) #['A', 'B']
print(g.minimumPath('A','C')) # ['A', 'B', 'C']
print(g.minimumPath('A','D'))  #['A', 'B', 'D']
print(g.minimumPath('A','E'))   #['A', 'B', 'E']
print(g.minimumPath('A','F'))   #['A', 'B', 'E', 'F']
print(g.minimumPath('A','G'))   #[]

print('minimum paths from G:')
print(g.minimumPath('G','A')) #[]
print(g.minimumPath('G','B')) #[]
print(g.minimumPath('G','C')) # []
print(g.minimumPath('G','D'))  #[G,D]
print(g.minimumPath('G','E'))   #[G,D,E]
print(g.minimumPath('G','F'))   #[G,D,E,F]
print(g.minimumPath('G','G'))   #[]
"""

import unittest

class Test(unittest.TestCase):
    #save mark
    mark=0
    
    def setUp(self):
        labels=['A', 'B', 'C', 'D', 'E','F','G']    
        # Create a given graph  
        self.g = Graph(labels)  
        self.g.addEdge('A', 'B')
        self.g.addEdge('B', 'C')
        self.g.addEdge('B', 'D')
        self.g.addEdge('B', 'E')
        self.g.addEdge('C', 'E')
        self.g.addEdge('D', 'E')
        self.g.addEdge('E', 'F')
        self.g.addEdge('G', 'D')

    def test_printMark(self):
        print('\n\n*************************')
        print("\n Provisional mark:",Test.mark)  
        print('*************************')

    def test1_minimumPath(self):
        print('Case 1: start==end ')
        self.assertEqual(self.g.minimumPath('A','A'), [])
        print('\t\t mark += 2')
        Test.mark+=2
        print()
    
    def test2_minimumPath(self):
        print('Case 2: No path ')
        self.assertEqual(self.g.minimumPath('A','G'), [])
        print('\t\t mark += 2')
        Test.mark+=2
        print()

    def test3_minimumPath(self):
        
        print('Case 3: path with distance 1')
        result=self.g.minimumPath('A','B')
        expected=['A','B']
        print('result:',result)
        print('expected:',expected)
        
        self.assertListEqual(result, expected)
        print('\t\t mark += 4')
        Test.mark+=4
        print()

    def test4_minimumPath(self):
        
        print('Case 4: path with distance 2')
        result=self.g.minimumPath('A','C')
        expected=['A','B','C']
        print('result:',result)
        print('expected:',expected)
        
        self.assertListEqual(result, expected)
        print('\t\t mark += 6')
        Test.mark+=6
        print()

    def test5_minimumPath(self):
        
        print('Case 4: path with distance 4')
        result=self.g.minimumPath('A','F')
        expected=['A', 'B', 'E', 'F']
        print('result:',result)
        print('expected:',expected)
        
        self.assertListEqual(result, expected)
        print('\t\t mark += 6')
        Test.mark+=6
        print()

 

#Google colab
#unittest.main(argv=['first-arg-is-ignored'], exit=False)

# Spyder
if __name__ == '__main__': 
    unittest.main()