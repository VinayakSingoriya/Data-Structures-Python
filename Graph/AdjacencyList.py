# Representation of Graph Data Structure through Adjacency List

# A class to represent the node of the adjancecy List
class adjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None]*self.V

    def add_edge(self, frm , to):
        node = adjNode(to)
        node.next = self.graph[frm]
        self.graph[frm] = node

        # Adding the source node to the destination
        #  as it is the undirected Graph
        node = adjNode(frm)
        node.next = self.graph[to]
        self.graph[to] = node

    def print_graph(self):
        for i in range(self.V):
            print(f"Adjacancy list of vertex {i} head", end = '')
            temp = self.graph[i]
            while temp:
                print(f"-> {temp.vertex}", end="")
                temp = temp.next
            print()

# Driver Mode
if __name__ == "__main__": 
    V = 5
    g = Graph(V)
    g.add_edge(0, 1)                     
    g.add_edge(0, 4)                     
    g.add_edge(1, 3)                     
    g.add_edge(1, 4)                     
    g.add_edge(2, 3)                     
    g.add_edge(3, 4)    
    g.add_edge(1, 2)                     
    g.print_graph()                 

