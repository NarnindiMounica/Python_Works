class GraphUsingEdgeList:

    def __init__(self):
        self.V = []
        self.edges = []

    def add_vertex(self, vertex):
        if vertex not in self.V:
            self.V.append(vertex)
        else:
            return f"{vertex} already exist"

    def add_edge(self, source, destination, weight=1):
        if source in self.V and destination in self.V:
            edge = (source, destination, weight)
            self.edges.append(edge)
        else:
            return "Either one or both vertices are not found"

