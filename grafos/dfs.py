# Estandar DFS
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


# DFS desde un vertice imprime una lista
def dfsVertex(self, key):
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
                    listaVertices.insert(0, self.vertices[current][j].vertex)
                j += 1
        print(visited)
    else:
        print("key does not exist in the graph")