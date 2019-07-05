class Node:
    def __init__(self, char: chr):
        self.val = char
        self.arr = dict()
        self.isWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(' ')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for char in word:
            if char not in root.arr:
                root.arr[char] = Node(char)
            
            root = root.arr[char]
        root.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for char in word:
            if char not in root.arr:
                return False
            root = root.arr[char]
        
        return root.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for char in prefix:
            if char not in root.arr:
                return False
            root = root.arr[char]
        
        return True

