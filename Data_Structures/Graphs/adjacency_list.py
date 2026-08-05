class GraphAdjacencyList:
    def __init__(self):
        self.vertices = []
        self.adj_list = {}

    def add_vertices(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.adj_list[vertex] = []
        else:
            return f"vertex {vertex} already exists"

    def add_edges(self, source, destination, weight=1):
        if source in self.vertices and destination in self.vertices:
            self.adj_list[source].append((destination, weight))
            self.adj_list[destination].append((source, weight))
        else:
            return "one or more vertices not found"    


            
