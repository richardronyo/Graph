class Node:
    """
    This implemetation of a Node uses an adjacency list format to list the edges. Instead of containing a pointer to the next node, this implementation contains a list of the indices of the end node in the overall Graph.
    Nodes are numbered in a counter-clockwise manner, in which the node located at 0 radians is first. My implementation makes possible for the use of an adjacency list when used in building a graph.


    Attributes:
        pos -> int
        data -> any data type Any kind of information desired to be stored
        edges -> {} of int
    """
    
    def __init__(self, pos, data = None):
        self.pos = pos
        self.data = data
        self.edges = set()

    def __str__(self):
        return f"Data: {self.data}\n\tEdges: {self.edges}"



if __name__ == "__main__":
    for i in range(5):
        new_node = Node(i)
        print(new_node)

    