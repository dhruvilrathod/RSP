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

s = initialize_union_find(10)
s = union(s,1,2)
s = union(s,2,4)
s = union(s,6,3)
s = union(s,7,3)
s = union(s,5,8)

print(s.parent)
print("check if 1 and 4 are friends (same component): ", same_component(s, 1,4))
print("check if 1 and 3 are friends (same component): ", same_component(s, 1,3))