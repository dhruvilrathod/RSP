class EdgeNode:
    def __init__(self, val, weight) -> None:
        self.val = val
        self.weight = weight
        self.next = None

class Graph:
    def __init__(self, total_nodes, directed) -> None:
        self.edge_nodes = [None] * total_nodes # this contains array of each node in the graph
        self.degrees = [0] * total_nodes # for each node, this stores the out-degree
        self.total_vertices = 0
        self.total_edges = 0
        self.directed = directed # checks if the graph is directed or un-directed


def initialize_graph(max_nodes, directed):
    return Graph(max_nodes, directed)


# Time complexity: O(1) constant amount of work
def insert_edge(g, x, y, directed, w=None):
    node = EdgeNode(y,w)

    # Now, Following steps to append this node in the graph
    node.next = g.edge_nodes[x]
    g.edge_nodes[x] = node
    g.degrees[x]+=1
    g.total_vertices+=1
    g.total_edges+=1
    
    if not directed:

        # same steps as above, to append a reverse edge node if the graph is undirected
        reverse_node = EdgeNode(x,w)
        reverse_node.next = g.edge_nodes[y]
        g.edge_nodes[y] = reverse_node
        g.degrees[x]+=1
        g.total_edges+=1
    
    return g

# Time Complexity: O(n + m)
def print_graph(g):
    for i in range(len(g.edge_nodes)):
        node = g.edge_nodes[i]
        if node:
            print(i, "::", end=" ")
            while node:
                print(node.val, " ", end=" -> ")
                node = node.next
            print()
        else:
            print(i)

g = None
MAX_VAL = 10

g = initialize_graph(MAX_VAL, False)
g = insert_edge(g,1,2,False)
g = insert_edge(g,1,3,False)
g = insert_edge(g,2,3,False)
g = insert_edge(g,2,4,False)
g = insert_edge(g,1,5,False)
g = insert_edge(g,6,3,False)
print_graph(g)
print("total vertices:", g.total_vertices)
print("total edges:", g.total_edges)