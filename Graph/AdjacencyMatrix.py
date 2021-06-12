# Representation of a graph Data structure through Adjacency Matrix

class Graph:
    def __init__(self, numvertex):
        self.adjMatrix = [[0]*numvertex for x in range(numvertex)]
        self.numvertex = numvertex
        self.vertices = {}
        self.verticesList = [0]*numvertex

    def set_vertex(self, vtx, id):
        if 0<=vtx<=self.numvertex:
            self.vertices[id] = vtx
            self.verticesList[vtx] = id

    def set_edge(self, frm, to):   # For weighted graph we can feed third parameter as cost and instead of 1 we can feed this cost in AdjMatrix
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to] =  1
        # for directed graph do not add this
        self.adjMatrix[to][frm] = 1

    def get_vertex(self):
        return self.verticesList

    def get_edges(self):
        edges = []
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if (self.adjMatrix[i][j]!=0):
                    edges.append((self.verticesList[i], self.verticesList[j]))
        return edges
    
    def get_matrix(self):
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                print(self.adjMatrix[i][j], end="  ")
            print()

# Driver Mode 
if __name__ == "__main__": 
    G = Graph(6)
    # Set vertices to a particular id
    G.set_vertex(0, 'a')     
    G.set_vertex(1, 'b')     
    G.set_vertex(2, 'c')     
    G.set_vertex(3, 'd')     
    G.set_vertex(4, 'e')     
    G.set_vertex(5, 'f')

    # set edeges between the vertices
    G.set_edge('a','e')
    G.set_edge('a','c')
    G.set_edge('c','b')
    G.set_edge('b','e')
    G.set_edge('e','d')
    G.set_edge('f','e')

    print(" \nVertices of a graph :")
    print(G.get_vertex())

    print(" \nEdeges of a graph: ")
    print(G.get_edges())

    print(" \nAdjancy Matrix of a graph:")
    print(G.get_matrix())


            