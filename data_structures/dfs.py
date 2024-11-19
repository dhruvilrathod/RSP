class Node:
    def __init__(self, val, weight=None):
        self.val = val
        self.weight = weight
        self.next = None

class Graph:
    def __init__(self, max_vertices, directed):
        self.vertices = [None]*max_vertices
        self.out_degrees = [0]*max_vertices
        self.directed = directed
        self.total_edges = 0
        self.total_vertices = 0

def initialize_graph(max_vertices, directed):
    return Graph(max_vertices, directed)

def insert_edge(g, x, y, directed, w=None):
    node1 = Node(y)
    node1.next = g.vertices[x]
    g.vertices[x] = node1
    g.out_degrees[x] += 1
    g.total_edges+=1

    if not directed:
        node2 = Node(x)
        node2.next = g.vertices[y]
        g.vertices[y] = node2
        g.out_degrees[y]+=1
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




# Following for DFS Traversal
def process_vertex_late(v):
    print("process late::", v)

def process_vertex_early(v):
    print("process early::", v)

def process_edge(v,y):
    print("process edge::", v, " <-> ", y)




def dfs(g, start):
    
    discovered[start] = True
    process_vertex_early(start)
    
    temp_node = g.vertices[start]
    while temp_node != None:
        temp = temp_node.val
        if not discovered[temp]:
            parent[temp] = start
            process_edge(start, temp)
            dfs(g, temp)
        elif (not processed[temp] and parent[start] != temp) or g.directed:
            process_edge(start,temp)
        temp_node = temp_node.next
    
    process_vertex_late(start)
    processed[start] = True






# Runner
g = None
MAX_VAL = 10

g = initialize_graph(MAX_VAL, False)
g = insert_edge(g,1,2,False)
g = insert_edge(g,1,8,False)
g = insert_edge(g,1,7,False)
g = insert_edge(g,2,3,False)
g = insert_edge(g,2,5,False)
g = insert_edge(g,2,7,False)
g = insert_edge(g,3,4,False)
g = insert_edge(g,5,4,False)
g = insert_edge(g,6,5,False)
print_graph(g)
print("total vertices:", g.total_vertices)
print("total edges:", g.total_edges)



discovered=[False]*(g.total_vertices + 1)
processed=[False]*(g.total_vertices + 1)
parent=[-1]*(g.total_vertices +1)
dfs(g,1)