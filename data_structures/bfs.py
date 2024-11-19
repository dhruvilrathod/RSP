class Node:
    def __init__(self, val, weight) -> None:
        self.val = val
        self.weight = weight,
        self.next = None


class Graph:
    def __init__(self, max_vertices, directed) -> None:
        self.directed = directed
        self.vertices = [None] * max_vertices
        self.out_degrees = [0] * max_vertices
        self.total_vertices = 0
        self.total_edges = 0


def initialize_graph(max_vertices, directed):
    return Graph(max_vertices, directed)

# Time complexity: O(1) constant amount of work
def insert_edge(g, v1, v2, directed, w=None):
    node1 = Node(v2, w)

    node1.next = g.vertices[v1]
    g.vertices[v1] = node1
    g.out_degrees[v1]+=1
    g.total_edges+=1

    if not directed:
        node2 = Node(v1,w)
        node2.next = g.vertices[v2]
        g.vertices[v2] = node2
        g.out_degrees[v2]+=1
        g.total_edges+=1
    
    g.total_vertices+=1
    return g

# Time Complexity: O(n + m)
def print_graph(g):
    for i in range(len(g.vertices)):
        node = g.vertices[i]
        if node:
            print(i, "::", end=" ")
            while node:
                print(node.val, " ", end=" -> ")
                node = node.next
            print()
        else:
            print(i)



# Following for BFS Traversal
def process_vertex_late(v):
    print("process late::", v)

def process_vertex_early(v):
    print("process early::", v)

def process_edge(v,y):
    print("process edge::", v, " <-> ", y)

def bfs(g, start_val):

    queue = [] # Queue of vertices to visit

    # To begin
    queue.append(start_val)
    discovered[start_val]=True

    # Logic
    while queue:
    
        v = queue.pop(0) # dequeue operation
        process_vertex_early(v)
        processed[v] = True # set it is processed
        temp_edge = g.vertices[v] # find for successor in adjacency list

        # Until it has successors
        while temp_edge != None:
            y = temp_edge.val
            
            # check if it is discovered
            if not discovered[y]:
                discovered[y] = True
                queue.append(y)
                parent[y]=v

            if not processed[y]:
                process_edge(v,y)

            temp_edge = temp_edge.next
        process_vertex_late(v)



# Runner
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



discovered=[False]*(g.total_vertices + 1)
processed=[False]*(g.total_vertices + 1)
parent=[-1]*(g.total_vertices +1)
bfs(g, 1)