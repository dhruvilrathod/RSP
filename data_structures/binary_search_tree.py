class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        
# Time complexity: O(1)
def create_binary_tree(val):
    return Node(val)


# Time Complexity: O(log n) => height of the tree log n
def insert_tree(tree, val):
    node = Node(val)
    if tree == None:
        return node
    if val < tree.val:
        if tree.left == None:
            tree.left = node
            node.parent = tree
        else:
            tree.left = insert_tree(tree.left, val)
    else:
        if tree.right == None:
            tree.right = node
            node.parent = tree
        else:
            tree.right = insert_tree(tree.right, val)
    return tree

# Time Complexity: O(log n) => height of the tree log n
def delete_tree(tree, val):
    if tree == None:
        return None
    
    # If a match found
    if tree.val == val:
        # Case: No children - just delete the node
        if (tree.right == None and tree.left == None):
            tree = None
        
        # Case: Both children: Find the in-order successor of node, replace it with node and delete it from the right sub tree
        elif (tree.right != None and tree.left != None):
            successor = find_successor(tree, val)
            tree.val = successor.val
            tree.right = delete_tree(tree.right, val)

        # Case: Any one child: Replace current node with that child
        else:
            if tree.left != None:
                tree = tree.left
            else:
                tree.right = None

    # For lower values, seach in right sub tree and delete
    elif tree.val < val:
        tree.right = delete_tree(tree.right, val)
    
    # For higher values, search in left sub tree and delete
    else:
        tree.left = delete_tree(tree.left, val)
    return tree

# Time Complexity: O(log n) => height of the tree log n
def find_successor(tree, val):
    successor = None
    in_order_traversal(tree, lambda x: process(x))
    def process(node):
        if node.val < val:
            nonlocal successor
            successor = node
    return successor


# Time Complexity: O(log n) => height of the tree log n
def search_tree(tree, val):
    if tree == None:
        return False
    if tree.val == val:
        return True
    if val < tree.val:
        return search_tree(tree.left, val)
    return search_tree(tree.right, val)

# Time Complexity: O(log n) => height of the tree log n
def in_order_traversal(tree, process_fn):
    if tree != None:
        in_order_traversal(tree.left, process_fn)
        process_fn(tree)
        in_order_traversal(tree.right, process_fn)

def post_order_traversal(tree, process_fn):
    if tree != None:
        post_order_traversal(tree.left, process_fn)
        post_order_traversal(tree.right, process_fn)
        process_fn(tree)


def post_order_traversal_iterative(tree, process_fn):
    if tree != None:
        stack = [tree]
        ans = []
        visited = set()
        while len(stack) > 0:
            top = stack[-1]
            print(top.val)
            has_children = False
            if top.right and not top.right in visited:
                has_children = True
                stack.append(top.right)
            if top.left and not top.left in visited:
                has_children = True
                stack.append(top.left)
            if not has_children:
                leaf = stack.pop(-1)
                ans.append(leaf.val)
                visited.add(leaf)
        return ans

tree = create_binary_tree(5)
tree = insert_tree(tree, 3)
tree = insert_tree(tree, 7)
tree = insert_tree(tree, 2)
tree = insert_tree(tree, 4)
tree = insert_tree(tree, 6)
tree = insert_tree(tree, 8)
tree = delete_tree(tree, 4)
# in_order_traversal(tree, lambda x: print("processing:: ", x.val))
post_order_traversal_iterative(tree, lambda x: print("processing:: ", x.val))
print("Searchiing for 4:", search_tree(tree, 4))
print("Searchiing for 14:", search_tree(tree, 14))