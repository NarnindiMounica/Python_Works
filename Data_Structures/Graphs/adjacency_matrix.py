class GraphAdjacencyMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [None] * num_vertices
        self.adj_matrix = [[None] * num_vertices for _ in range(num_vertices)]

    def add_vertex(self, index, label):
        if index >= 0 and index < self.num_vertices:  
            self.vertices[index] = label
        else:
            return "Index OOB"  

    def add_edge(self, source, destination, weight=1):
        if 0 <= source < self.num_vertices and 0 <= destination < self.num_vertices:
            self.adj_matrix[source][destination] = weight
            self.adj_matrix[destination][source] = weight    