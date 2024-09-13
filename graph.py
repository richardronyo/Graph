from node import Node
import matplotlib.pyplot as plt
import numpy as np
import math

class Graph:
    """
    This implementation of a Graph uses a list to store it's nodes instead of pointers. This is reflective of using an adjacency list.
    Nodes are numbered in a counter-clockwise manner, in which it starts with the node located at 0 radians on the unit circle.

    Attributes:
        nodes -> [] of Node objects
        n -> Number of nodes
        data -> A list of the data belonging to each Node
    """
    def __init__(self, n, data = None):
        self.nodes = []
        self.n = 0
        self.adjacency_matrix = np.zeros((n, n))


        for i in range(n):
            if data == None:
                self.nodes.append(Node(i))
            else:
                self.nodes.append(Node(i, data[i]))

            self.adjacency_matrix[i, i] = 1
            self.n += 1

    def __str__(self):
        graph_str = f""

        for i in range(self.n):
            graph_str += f"Node {i + 1}:\n\t{self.nodes[i]}\n"

        graph_str += f"Adjacency Matrix:\t{self.adjacency_matrix.shape}\n{self.adjacency_matrix}"
        return graph_str
    
    def edge(self, pos1, pos2):
        self.nodes[pos1].edges.add(pos2)
        self.nodes[pos1].edges.add(pos2)

        self.adjacency_matrix[pos1, pos2] = 1
        self.adjacency_matrix[pos2, pos1] = 1

    def complete(self):
        if self.n > 1:
            for i in range(self.n):
                for j in [index for index in range(self.n) if index != i]:
                    self.edge(i, j)
                
    def compute_coord(self, radius = 1):
        coord = []

        for i in range(self.n):
            x = radius * math.cos(2 * math.pi * i / self.n)
            y = radius * math.sin(2 * math.pi * i / self.n)

            coord.append((x, y))

        return coord
    
    def visualize(self):
        fig, ax = plt.subplots()

        coord = self.compute_coord()

        #This portion of code draws the edges
        for node in self.nodes:
            for edge in node.edges:
                x_values = [coord[node.pos][0], coord[edge][0]]
                y_values = [coord[node.pos][1], coord[edge][1]]
                ax.plot(x_values, y_values, 'k-', lw=1)

        # Plot nodes
        for node in self.nodes:
            ax.plot(coord[node.pos][0], coord[node.pos][1], 'bo', markersize=10)  # Draw nodes as blue circles
            ax.text(coord[node.pos][0] + 0.05, coord[node.pos][1] + 0.05, str(node.pos + 1), fontsize=12)  # Label nodes

        # Set equal aspect ratio and limits to make the graph look proportional
        ax.set_aspect('equal')
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)

        # Add a title and show the plot
        plt.title(f"{self.n}-gon Graph")
        plt.show()

    



if __name__ == "__main__":
    for i in range(8):
        ki = Graph(i + 1)
        ki.complete()
        print(ki)

        ki.visualize()
