# Search for a minimum spanning tree in a graph
# Useful for a dense graph
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


# Time Complexity: O(m * 2n) = O(mn)
def prim(g, start):
    
    intree=[False]*g.max_nodes
    distance=[float('inf')]*g.max_nodes
    parent=[-1]*g.max_nodes
    temp_dist = float('inf')
    total_mst_weight=0

    v=start
    parent[start]=0

    while not intree[v]:
        intree[v]=True

        temp = g.vertices[v]


        if (v != start):
            print("added edge: ", parent[v], '-', v)
            total_mst_weight+=temp_dist

        # This will store every possible candidate element with their weight and parent
        while temp != None:
            candidate = temp.val
            if temp.weight < distance[candidate] and not intree[candidate]:
                distance[candidate] = temp.weight
                parent[candidate] = v
            temp = temp.next
        
        temp_dist = float('inf')
        
        # now, for all vertices, we check for the minimum distance which is not yet entered in tree
        for i in range(g.total_vertices):
            if (not intree[i]) and (distance[i] < temp_dist):
                temp_dist = distance[i]
                v=i

        
    return total_mst_weight

g = initialize_graph(10,False)
# g = insert_graph(g,1,2,False, 1)
# g = insert_graph(g,1,8,False, 2)
# g = insert_graph(g,1,7,False, 3)
# g = insert_graph(g,2,3,False, 9)
# g = insert_graph(g,2,5,False, 8)
# g = insert_graph(g,2,7,False, 2)
# g = insert_graph(g,3,4,False, 4)
# g = insert_graph(g,5,4,False, 7)
# g = insert_graph(g,6,5,False, 6)

g = insert_graph(g,0,1,False, 4)
g = insert_graph(g,0,4,False, 6)
g = insert_graph(g,0,3,False, 6)
g = insert_graph(g,0,2,False, 4)
g = insert_graph(g,1,2,False, 2)
g = insert_graph(g,2,3,False, 8)
g = insert_graph(g,3,4,False, 9)

total = prim(g, 1)
print("Total weight:", total)