import sys


class AdjacentVertex:
    """Note: Instead of using this class, you could use a tuple"""

    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    def __str__(self):
        return '(' + str(self.vertex) + ',' + str(self.weight) + ')'


class Graph():
    def __init__(self, labels, directed=True):
        """We use a dictionary to represent the graph
        the dictionary's keys are the vertices
        The value associated for a given key will be the list of their neighbours.
        Initially, the list of neighbours is empty"""
        self.vertices = {}
        for v in labels:
            self.vertices[v] = []
        self.directed = directed

    def addEdge(self, start, end, weight=0):
        if start not in self.vertices:
            print(start, ' does not exist!')
            return
        if end not in self.vertices:
            print(end, ' does not exist!')
            return

        # adds to the end of the list of neigbours for start
        self.vertices[start].append(AdjacentVertex(end, weight))

        if self.directed == False:
            # adds to the end of the list of neigbours for end
            self.vertices[end].append(AdjacentVertex(start, weight))

    def containsEdge(self, start, end):
        if start not in self.vertices:
            print(start, ' does not exist!')
            return -1
        if end not in self.vertices:
            print(end, ' does not exist!')
            return -1

        # we search the AdjacentVertex whose v is end
        for adj in self.vertices[start]:
            if adj.vertex == end:
                if adj.weight != 0:
                    return adj.weight
                else:
                    return 1  # unweighted graphs
        return 0  # does not exist

    def removeEdge(self, start, end):
        if start not in self.vertices:
            print(start, ' does not exist!')
            return
        if end not in self.vertices:
            print(end, ' does not exist!')
            return
        for adj in self.vertices[start]:
            if adj.vertex == end:
                self.vertices[start].remove(adj)
        if self.directed == False:
            for adj in self.vertices[end]:
                if adj.vertex == start:
                    self.vertices[end].remove(adj)

    def minDistance(self, distances, visited):
        min = sys.maxsize
        for i in self.vertices:
            if distances[i] <= min and visited[i] == False:
                min = distances[i]
                min_index = i

        return min_index

    def __str__(self):
        result = ''
        for v in self.vertices:
            result += '\n' + str(v) + ':'
            for adj in self.vertices[v]:
                result += str(adj)

        return result