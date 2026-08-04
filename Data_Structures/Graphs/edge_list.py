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

    def display(self):
        print("Vertices")

        for vertex in self.V:
            print(f"Vertex: {vertex}") 

        for source, destination, weight in self.edges:
            print(f"{source} ---> {destination}")       


graph = GraphUsingEdgeList()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)

graph.add_edge(1,2,1)
graph.add_edge(2,3,1)

graph.display()


