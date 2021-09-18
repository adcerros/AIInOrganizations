import sys


def dijkstra(self, origin):
    visited = {}

    for v in self.vertices.keys():
        visited[v] = False
    previous = {}

    for v in self.vertices.keys():
        previous[v] = -1
    distances = {}

    for v in self.vertices.keys():
        distances[v] = sys.maxsize
    distances[origin] = 0

    for n in range(len(self.vertices)):
        u = self.minDistance(distances, visited)
        visited[u] = True

        for adj in self.vertices[u]:
            i = adj.vertex
            w = adj.weight
            if visited[i] == False and distances[i] > distances[u] + w:
                distances[i] = distances[u] + w
                previous[i] = u

    self.printSolution(distances, previous, origin)