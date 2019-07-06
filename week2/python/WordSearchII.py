class Node:
    def __init__(self, char: chr):
        self.val = char
        self.arr = dict()
        self.isWord = False
        
class Trie:
    def __init__(self):
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
        
        return True

    
class Solution:
    
    def dfs(self, board: List[List[str]], x: int, y: int, root: Node, visited: set, word: List[str], ans: set()) -> bool:
        if x<0 or x>=len(board) or y<0 or y>=len(board[x]) or (x,y) in visited:
            return
        
        char = board[x][y]
        if char not in root.arr:
            return
        
        word += list(char)

        if root.arr[char].isWord:
            ans.add(''.join(word))

        visited.add((x,y))
        for (i,J) in [(-1,0),(1,0),(0,-1),(0,1)]:
            self.dfs(board,x+i,y+J,root.arr[char],visited, word,ans) 
        
        visited.remove((x,y))
        word.pop()
            
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.insert(word)
        
        ans = set()
        for i in range(0, len(board),1):
            for j in range(0, len(board[i]), 1):
                word=list()
                self.dfs(board,i,j,trie.root,set(),word,ans)

        return list(ans)
