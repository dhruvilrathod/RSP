class TrieNode:
    def __init__(self) -> None:
        self.children = [None]*26
        self.is_leaf = False

def initialize_trie():
    return TrieNode()

# Time Complexity: O(n), n = length of the word
def insert_word(t, word):
    if word != "":
        index = ord(word[0]) - ord('a')
        if not t.children[index]:
            t.children[index] = TrieNode()
        t.children[index] = insert_word(t.children[index], word[1:])
        if word[1:] == "":
            t.is_leaf = True
    return t        


def print_all(t, string=""):
    length = len(t.children)
    for i in range(length):
        if t.children[i] != None:
            char = chr(i+ord('a'))
            print(char, end = "")
            print_all(t.children[i])
    print()
    return


# Time Complexity: O(n) worst case
def search_word(t, word):
    if word == "" or not t.children:
        return False
    index = ord(word[0])-ord('a')
    if not t.children[index]:
        return False
    if t.children[index] != None and t.is_leaf:
        return True
    return search_word(t.children[index], word[1:])
    


t = initialize_trie()
t = insert_word(t, "and")
t = insert_word(t, "ant")
print("searching ant: ", search_word(t, 'ant'))
print("searching ani: ", search_word(t, 'ani'))
print_all(t)