class GraphUsingEdgeList:

    def __init__(self):
        self.V = []
        self.edges = []

    def add_vertex(self, vertex):
        if vertex not in self.V:
            self.V.append(vertex)
