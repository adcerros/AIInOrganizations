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


# BFS desde un vertice imprime una lista
def bfsVertex(self, key):
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