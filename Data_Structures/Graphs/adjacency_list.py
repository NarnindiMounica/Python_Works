class GraphAdjacencyList:
    def __init__(self):
        self.vertices = []
        self.adj_list = []

    def add_vertices(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
        else:
            return f"vertex {vertex} already exists"

            
