class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        parents = {}
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if r==0 or r==len(board)-1 or c==0 or c==len(board[r])-1:
                    self.dfs(board, parents, r, c, -1, -1)
        
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == 'O' and parents.get((r,c)) != (-1, -1):
                    board[r][c] = 'X' 
    
    def find(self, a , parents):
        if a not in parents:
            parents[a] = a
        else:
            while a in parents and a != parents[a]:
                parents[a] = parents[parents[a]]
                a = parents[a]
        
        return a
    
    def dfs(self,board,parents,r,c,prevR, prevC):
        if (r,c) in parents or r<0 or r>=len(board) or c<0 or c>=len(board[0]) or board[r][c] != 'O':
            return
        
        rootPrev = self.find((prevR,prevC), parents)
        rootCur = self.find((r,c), parents)
        if rootPrev != rootCur:
            parents[rootCur] = rootPrev

        self.dfs(board,parents,r-1,c,r,c)
        self.dfs(board,parents,r+1,c,r,c)
        self.dfs(board,parents,r,c-1,r,c)
        self.dfs(board,parents,r,c+1,r,c)