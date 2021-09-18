from ExamenFinalEDA.grafos.graphConLabels import Graph
from ExamenFinalEDA.grafos.graphConLabels import AdjacentVertex


class grafoDivisores(Graph):

    #Inicializa un grafo
    def __init__(self, labels, directed=True):
        self.vertices = {}
        for v in labels:
            self.vertices[v] = []
        self.directed = directed

    #Añade una conexion entre vertices
    def añadirConexion(self, start, end, weight=0):
        if start not in self.vertices:
            print(start, ' does not exist!')
            return
        if end not in self.vertices:
            print(end, ' does not exist!')
            return
        self.vertices[start].append(AdjacentVertex(end, weight))
        if self.directed == False:
            self.vertices[end].append(AdjacentVertex(start, weight))

    #Dada una clave imprime sus vertices adyacentes
    def imprimirAdyacentes(self,elem):
        if elem ==None:
            return
        else:
            i=0
            while i < len(self.vertices[elem]):
                print(self.vertices[elem][i].vertex)
                i += 1

    #Dada cierta clave retorna una lista con sus adyacentes
    def listaAdyacentes(self,elem):
        if elem ==None:
            return
        else:
            adyacentes = []
            i=0
            while i < len(self.vertices[elem]):
                adyacentes.append(self.vertices[elem][i].vertex)
                i += 1
            return adyacentes

    #Dada cierta clave imrpime las claves que la contienen en sus adyacentes si el grafo es dirijido es decir los que le apuntan
    def imprimirAdyacentesDirected(self,elem):
        if self.directed == True:
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
        else:
            return self.imprimirAdyacentes()

    #Dada cierta clave devuelve una lista de las claves que la contienen en sus adyacentes si el grafo es dirijido es decir los que le apuntan
    def listaAdyacentesDirected(self,elem):
        if self.directed == True:
            if elem ==None:
                return
            else:
                adyacentes = []
                i=0
                keys = list(self.vertices.keys())
                while i < len(self.vertices)-1:
                    j=0
                    i += 1
                    while j < len(self.vertices[i]):
                        if self.vertices[i][j].vertex == elem:
                            adyacentes.append(keys[i])
                        j +=1
                return adyacentes
        else:
            return self.listaAdyacentes()

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

    def bfs(self):
        visited = {}
        for v in self.vertices.keys():
            visited[v] = False
        for v in self.vertices.keys():
            if visited[v] == False:
                self._bfs(v, visited)

    # Function to print a BFS of graph
    def _bfs(self, v, visited):
        queue = []
        visited[v] = True
        queue.append(v)
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for adj in self.vertices[s]:
                if visited[adj.vertex] == False:
                    queue.append(adj.vertex)
                    visited[adj.vertex] = True

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
for i in range(0,39):
    grafo.añadirConexion(i-1,i+1,0)
grafo.dfs()
grafo.bfs()
print()
grafo.dfsVertex(1)
grafo.bfsVertex(1)
grafo.imprimirAdyacentes(2)
print(grafo.numeroConexiones())