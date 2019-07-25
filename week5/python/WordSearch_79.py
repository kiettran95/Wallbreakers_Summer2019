class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        def dfs(x: int, y: int, index: int) -> bool:
            if index == len(word):
                return True
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[x]) \
                or (x,y) in visited or board[x][y] != word[index]:
                return False
            
            index +=1
            visited.add((x,y))
            if dfs(x-1,y,index) or dfs(x+1,y,index) \
                or dfs(x,y-1,index) or dfs(x,y+1,index):
                return True
            
            visited.remove((x,y))
            return False
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if (r,c) not in visited and dfs(r,c,0):
                    return True
                
        return False
