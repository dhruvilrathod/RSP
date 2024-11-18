class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

# Time complexity: O(1)
def create_linked_list(val):
    return Node(val)

# Time complexity: O(1)
def insert_list(ll, val):
    new_node = Node(val)
    ll.prev = new_node
    new_node.next = ll
    return new_node

# Time complexity: O(n)
def delete_list(ll, val):
    if ll == None:
        return None
    if ll.val == val:
        if ll.next:
            ll.next.prev = None
            return ll.next
        else:
            return ll
    start = ll
    while start.next != None:
        start = start.next
        if (start.val == val):
            if start.next:
                start.next.prev = start.prev
                start.prev.next = start.next
            else:
                start.prev.next = None
            break
    return ll


# Time complexity: O(n)
def search_list(ll, val):
    if ll == None:
        return False
    if ll.val == val:
        return True
    while ll.next:
        ll = ll.next
        if ll.val == val:
            return True
    return False

# Time complexity: O(n)
def display_list(ll):
    print("Doubly Linked list::")
    while ll != None:
        print(" " + str(ll.val) + " ", end="")
        ll = ll.next


ll1 = create_linked_list(5)
ll1 = insert_list(ll1, 4)
ll1 = insert_list(ll1, 6)
ll1 = insert_list(ll1, 1)
ll1 = insert_list(ll1, 8)
ll1 = delete_list(ll1, 4)
ll1 = delete_list(ll1, 14)
display_list(ll1)
print("Searching for 4: ", search_list(ll1, 4))
print()
print("Searching for 1: ", search_list(ll1, 1))