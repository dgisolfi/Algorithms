


class BellmanFord:
    def __init__(self, graph, vertex, weight):
        self.__graph = graph
        self.__source_vertex = vertex
        self.__source_weight = weight
        self.initSingleSource(self.__graph, self.__source_vertex)

    def initSingleSource(self, graph, source_vertex):
        for vertex in graph.vertices:
            # estimate of shortest path distance
            vertex.distance = 'infinity'
            # previous vertex
            vertex.predecessor = None
        source_vertex.distance = 0
        print(self.__source_vertex.distance)

        
        