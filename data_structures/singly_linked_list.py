class Node:
    def __init__(self, val):
        self.val=val
        self.next=None

# Time complexity: O(1)
def create_linked_list(starting_value):
    return Node(starting_value)

# Time complexity: O(1)
def insert_list(ll, value):
    temp = Node(value)
    temp.next = ll
    return temp

# Time complexity: O(n)
def delete_list(ll, value):
    if ll == None:
        return None
    elif ll.val == value:
        ll=ll.next
        return ll
    prev = None
    start = ll
    while start.next != None:
        prev = start
        start = start.next
        if start.val == value:
            prev.next = start.next
            break
    return ll

# Time complexity: O(n)
def search_list(ll, value):
    if ll == None:
        return False
    elif ll.val == value:
        return True
    start = ll
    while start.next != None:
        start = start.next
        if start.val == value:
            return True
    return False

# Time complexity: O(n)
def display_list(ll):
    print("Linked list::")
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