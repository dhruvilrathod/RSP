import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1 # initially any node will have the height 1, when root is created

# Time Complexity: O(1)
def initialize_tree(val):
    return Node(val)

# Time Complexity: O(1)
def get_height(tree):
    if tree == None:
        return 0
    return tree.height

# Time Complexity: O(log n)
def calculate_balance_factor(tree):
    if tree == None:
        return 0
    return get_height(tree.left) - get_height(tree.right)

# Time Complexity: O(log n)
def getMin(tree):
    if tree == None or tree.left == None:
        return tree
    return getMin(tree.left)

# Time Complexity: O(log n)
def insert_node(tree,val):
    node = Node(val)
    if tree == None:
        return node
    elif val < tree.val:
        tree.right = insert_node(tree.right, val)
    else:
        tree.left = insert_node(tree.left, val)
    
    # update the height for future calculation reference
    tree.height = max(get_height(tree.right), get_height(tree.left)) + 1

    # get the balance factor
    balance = calculate_balance_factor(tree)

    if balance > 1: # something wrong in left side
        if val < tree.left.val:
            # TO DO: R-Rotation (it was inserted linearly left side)
            tree = right_rotation(tree)
        else:
            # TO DO: LR-Rotation (it was inserted somewhere root->left->right)
            tree.left = left_rotation(tree.left)
            tree = right_rotation(tree)
    elif balance < -1: # something wrong in right side
        if val > tree.right:
            # TO DO: L-Rotation (it was inserted linearly right side)
            tree = left_rotation(tree)
        else:
            # TO DO: RL-Rotation (it was inserted somewhere root->right->left)
            tree.right = right_rotation(tree.right)
            tree = left_rotation(tree)
    return tree

# Time Complexity: O(log n)
def delete_node(tree, val):
    if tree == None:
        return tree
    
    if val < tree.val:
        tree.left = delete_node(tree.left, val)
    elif val > tree.val:
        tree.right = delete_node(tree.right, val)
    elif val == tree.val:

        # if node has any one child, then make it the node
        if tree.left == None:
            tree = tree.right
            return tree
        elif tree.right == None:
            tree = tree.left
            return tree
        
        # Otherwise, find the minimum value node, on the right sub tree, make it the current root node, and delete it from right sub tree
        temp = getMin(tree.right)
        tree.val = temp.val
        tree.right = delete_node(tree.right, temp.val)

        # Re balance the tree if the balance factor of root is not -1,0,1
        balance = calculate_balance_factor(tree)
        if balance > 1: # something is wrong with left sub tree

            # rules
            if calculate_balance_factor(tree.left) >= 0:
                # perform a R-Rotation for the root
                tree = right_rotation(tree)
            else:
                # perform LR-Rotation for the root
                tree.left = left_rotation(tree.left)
                tree = right_rotation(tree)

        elif balance < -1: # something is wrong with the right sub tree
            # rules
            if calculate_balance_factor(tree.right) <= 0:
                # perform a L-Rotation for the root
                tree = left_rotation(tree)
            else:
                # perform RL-Rotation for the root
                tree.right = right_rotation(tree.right)
                tree = left_rotation(tree)
    
    return tree
    
def left_rotation(node):
    right = node.right
    temp = right.left
    right.left = node
    node.right = temp

    # change height:
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    right.height = 1 + max(get_height(right.left), get_height(right.right))

def right_rotation(node):
    left = node.left
    temp = left.right
    left.right = node
    node.left = temp

    # change height:
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    left.height = 1 + max(get_height(left.left), get_height(left.right))


# Print the tree
def printHelper(currPtr, indent, last):
    if currPtr != None:
        sys.stdout.write(indent)
        if last:
            sys.stdout.write("R--->")
            indent += "     "
        else:
            sys.stdout.write("L--->")
            indent += "|    "
        print(currPtr.val)
        printHelper(currPtr.left, indent, False)
        printHelper(currPtr.right, indent, True)


tree = initialize_tree(33)
tree = insert_node(tree, 13)
tree = insert_node(tree, 52)
tree = insert_node(tree, 9)
tree = insert_node(tree, 21)
tree = insert_node(tree, 61)
tree = insert_node(tree, 8)

tree = delete_node(tree,33)

printHelper(tree, "", True)
