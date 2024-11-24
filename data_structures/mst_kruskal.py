# Search for a minimum spanning tree in a graph
# Useful for a sparse graph
# Greedy

class Node:
    def __init__(self,val,weight=None) -> None:
        self.val = val
        self.weight = weight
        self.next=None

class Graph:
    def __init__(self,max_nodes,directed) -> None:
        self.max_nodes=max_nodes
        self.vertices=[None]*max_nodes
        self.out_degrees=[0]*max_nodes
        self.directed=directed
        self.total_vertices=0
        self.total_edges=0

def initialize_graph(max_nodes, directed):
    return Graph(max_nodes, directed)

def insert_graph(g,v1,v2,directed,weight=None):
    node1 = Node(v2,weight)
    node1.next=g.vertices[v1]
    g.vertices[v1]=node1
    g.out_degrees[v1]+=1
    g.total_edges+=1

    if not directed:
        node2=Node(v1,weight)
        node2.next = g.vertices[v2]
        g.vertices[v2] = node2
        g.out_degrees[v2]+=1
        g.total_edges+=1
    
    g.total_vertices+=1
    return g



# Union-find
class UnionFind:
    def __init__(self, set_size) -> None:
        self.parent=[] # parent vertex of current vertex i/sub-tree
        self.size=[] # size of current vertex i/subtree
        self.total = set_size

def initialize_union_find(total_vertex):
    s = UnionFind(total_vertex)
    for i in range(total_vertex):
        s.parent.append(i)
        s.size.append(1)
    return s

def find(s, val):
    if s.parent[val] == val:
        return val
    return find(s, s.parent[val])

def union(s, s1, s2):
    r1 = find(s, s1)
    r2 = find(s, s2)

    if r1 != r2:
        # check the size and append the smaller one to the bigger one
        if s.size[r1] >= s.size[r2]:
            s.parent[r2]=r1
            s.size[r1]+=s.size[r2]
        else:
            s.parent[r1]=r2
            s.size[r2]+=s.size[r1]

    return s

def same_component(s, s1, s2):
    return find(s,s1) == find(s,s2)

def to_edge_list(g):
        edge_list = []
        for u in range(len(g.vertices)):
            temp = g.vertices[u]
            while temp:
                v = temp.val
                weight = temp.weight
                if u < v:  # Making sure that no duplicate edges in the undirected graph
                    edge_list.append((u, v, weight))
                temp = temp.next
        return edge_list


# Time Complexity: O(m log m)
def kruskal(g):
    s = initialize_union_find(g.total_vertices)
    edges = to_edge_list(g)
    edges.sort(key=lambda x: x[2]) 
    total_mst_weight=0
    mst_edges = []

    for edge in edges:
        u, v, weight = edge
        if not same_component(s, u, v):
            print("adding: ", u,'-',v, 'with wieght', weight)
            total_mst_weight += weight
            mst_edges.append((u, v))
            s = union(s, u, v)

    return total_mst_weight


g = initialize_graph(10,False)

g = insert_graph(g,0,1,False, 4)
g = insert_graph(g,0,4,False, 6)
g = insert_graph(g,0,3,False, 6)
g = insert_graph(g,0,2,False, 4)
g = insert_graph(g,1,2,False, 2)
g = insert_graph(g,2,3,False, 8)
g = insert_graph(g,3,4,False, 9)

total = kruskal(g)
print("Total weight:", total)