class Node:
    def __init__(self, data):
        self.data = data
        self.edges = []

    def __str__(self):
        return f"Data:{self.data}\n\tEdges:{self.edges}"



if __name__ == "__main__":
    for i in range(5):
        new_node = Node(i)
        print(new_node)

    