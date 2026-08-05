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

    def display(self):
        print("Vertices:")
        for vertex in self.vertices:
            print(f"Vertex: {vertex}")

        for vertex in self.adj_list.keys():
            print(f"{vertex} ---> {self.adj_list[vertex]}")          

graph = GraphAdjacencyList()
graph.add_vertices('A')
graph.add_vertices('B')
graph.add_vertices('C')
graph.add_vertices('D')
graph.add_vertices('E')

graph.add_edges('A', 'B', 1 )
graph.add_edges('A', 'C', 1 )
graph.add_edges('B', 'D', 1 )

graph.display()


            
