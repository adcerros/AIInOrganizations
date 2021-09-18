from ExamenFinalEDA.grafos.graphConLabels import Graph
from ExamenFinalEDA.grafos.graphConLabels import AdjacentVertex


class grafoDivisores(Graph):

    #Inicializa un grafo con los divisores de 1 a n, la relacion divisor de es representada por los vertices
    def __init__(self, labels, directed=False):
        self.vertices = {}
        for v in labels:
            self.vertices[v] = []
        self.directed = directed
        keys = self.vertices.keys()
        for key in keys:
            for num in keys:
                 if key != num and num != 0:
                     if key % num == 0:
                        self.vertices[key].append(AdjacentVertex(num,0))

    #Dado cierto numero imprime sus divisores
    def imprimirDivisores(self,elem):
        if elem ==None:
            return
        else:
            i=0
            while i < len(self.vertices[elem]):
                print(self.vertices[elem][i].vertex)
                i += 1

    #Dado cierto numero returna una lista con sus divisores
    def listaDivisores(self,elem):
        if elem ==None:
            return
        else:
            divisores = []
            i=0
            while i < len(self.vertices[elem]):
                divisores.append(self.vertices[elem][i].vertex)
                i += 1
            return divisores

    #Dado cierto numero imprime sus multiplos
    def imprimirMultiplos(self,elem):
        if elem ==None:
            return
        else:
            i=0
            keys = list(self.vertices.keys())
            while i < len(self.vertices)-1:
                j=0
                i += 1
                while j < len(self.vertices[i]):
                    if self.vertices[i][j].vertex == elem:
                        print(keys[i])
                    j +=1

    #Dado cierto numero returna una lista con sus multiplos
    def listaMultiplos(self,elem):
        if elem ==None:
            return
        else:
            multiplos = []
            i=0
            keys = list(self.vertices.keys())
            while i < len(self.vertices)-1:
                j=0
                i += 1
                while j < len(self.vertices[i]):
                    if self.vertices[i][j].vertex == elem:
                        multiplos.append(keys[i])
                    j +=1
            return multiplos

    #Estandar DFS
    def dfs(self):
        visited = {}
        for v in self.vertices.keys():
            visited[v] = False

        for v in self.vertices.keys():
            if visited[v] == False:
                self._dfs(v, visited)
        print()

    def _dfs(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for adj in self.vertices[v]:
            if visited[adj.vertex] == False:
                self._dfs(adj.vertex, visited)

    #DFS desde un vertice imprime una lista
    def dfsVertex(self,key):
        keys = list(self.vertices.keys())
        if keys.__contains__(key) == True:
            listaVertices = []
            visited = []
            listaVertices.append(key)
            while not len(listaVertices) == 0:
               current = listaVertices.pop(0)
               if current not in visited:
                   visited.append(current)
               j = 0
               while j < len(self.vertices[current]):
                    if self.vertices[current][j].vertex not in visited:
                        listaVertices.insert(0,self.vertices[current][j].vertex)
                    j += 1
            print(visited)
        else:
            print("key does not exist in the graph")

    #BFS desde un vertice imprime una lista
    def bfsVertex(self,key):
        keys = list(self.vertices.keys())
        if keys.__contains__(key) == True:
            listaVertices = []
            visited = []
            listaVertices.append(key)
            while not len(listaVertices) == 0:
               current = listaVertices.pop(0)
               if current not in visited:
                   visited.append(current)
               j = 0
               while j < len(self.vertices[current]):
                    if self.vertices[current][j].vertex not in visited:
                        listaVertices.append(self.vertices[current][j].vertex)
                    j += 1
            print(visited)
        else:
            print("key does not exist in the graph")

    # Imprime los vertices y sus relaciones con sus pesos
    def imprimirGrafo(self):
        keys = list(self.vertices.keys())
        for key in keys:
            print("La clave es: " + str(key))
            i=0
            while i < len(self.vertices[key]):
                print("\tAdyacente con: ")
                print("\t\t" + str(self.vertices[key][i].vertex) + " con coste " + str(self.vertices[key][i].weight))
                i += 1

    #Retorna el numero de conexiones del grafo
    def numeroConexiones(self):
        numeroConexiones = 0
        keys = list(self.vertices.keys())
        for key in keys:
            numeroConexiones += len(self.vertices[key])
        if self.directed == True:
            return numeroConexiones
        else:
            return numeroConexiones // 2

data = []
for i in range(0,40):
    data.append(i)
grafo = grafoDivisores(data)
grafo.dfs()
grafo.dfsVertex(30)
grafo.bfsVertex(2)
print(grafo.numeroConexiones())
