from node import Node


class Graph:
    def __init__(self, n):
        self.nodes = []
        self.n = 0

        for i in range(n):
            self.nodes.append(Node(i))
            self.n += 1

    def edge(self, node1, node2):
        self.nodes[node1].edges.append(node2)
        self.nodes[node2].edges.append(node1)
    
    def __str__(self):
        graph_str = f""

        for i in range(self.n):
            graph_str += f"Node {i}:\n\t{self.nodes[i]}\n"

        return graph_str
    

if __name__ == "__main__":
    graph = Graph(5)

    for i in range(5):
        graph.edge(i, 4 - i)

    print(graph)