import networkx as nx
import matplotlib.pyplot as plt

MAXV = 100

class EdgeNode:
    def __init__(self, y, weight=0, next_node=None):
        self.y = y
        self.weight = weight
        self.next = next_node

class Graph:
    def __init__(self, directed=False):
        self.edges = [None] * (MAXV + 1)
        self.degree = [0] * (MAXV + 1)
        self.nvertices = 0
        self.nedges = 0
        self.directed = directed

    def initialize_graph(self, directed):
        self.nvertices = 0
        self.nedges = 0
        self.directed = directed

        for i in range(1, MAXV + 1):
            self.degree[i] = 0
            self.edges[i] = None

    def read_graph(self, directed):
        self.initialize_graph(directed)
        self.nvertices, m = map(int, input("Enter number of vertices and edges: ").split())
        
        for i in range(1, m + 1):
            x, y = map(int, input("Enter edge (x, y): ").split())
            self.insert_edge(x, y, directed)

    def insert_edge(self, x, y, directed):
        new_edge = EdgeNode(y)
        new_edge.next = self.edges[x]
        self.edges[x] = new_edge
        self.degree[x] += 1

        if not directed:
            self.insert_edge(y, x, True)
        else:
            self.nedges += 1

    def print_graph(self):
        for i in range(1, self.nvertices + 1):
            print(f"{i}:", end=" ")
            p = self.edges[i]

            while p is not None:
                print(f" {p.y}", end="")
                p = p.next
            print()
    
    def visualize_graph(self):
        G = nx.DiGraph() if self.directed else nx.Graph()
        
        # Add edges to the graph
        for i in range(1, self.nvertices + 1):
            p = self.edges[i]
            while p is not None:
                G.add_edge(i, p.y)  # add edge from i to p.y
                p = p.next

        # Draw the graph using networkx and matplotlib
        pos = nx.spring_layout(G)  # positions for all nodes
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black', edge_color='gray')
        plt.show() 
g = Graph()
g.read_graph(directed=False)
g.print_graph()
g.visualize_graph()
