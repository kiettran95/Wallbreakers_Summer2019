class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        n,m = len(matrix), len(matrix[0])
        dp = [[0]*m for _ in range(n)]        
        def dfs(x: int, y: int) -> int:
            if not dp[x][y]:
                cur_value = matrix[x][y]
                dp[x][y] = 1 + max(dfs(x-1,y) if x and matrix[x-1][y]<cur_value else 0, \
                            dfs(x+1,y) if x+1<n and matrix[x+1][y]<cur_value else 0, \
                            dfs(x,y-1) if y>0 and matrix[x][y-1]<cur_value else 0, \
                            dfs(x,y+1) if y+1<m and matrix[x][y+1]<cur_value else 0)
            return dp[x][y]
        
        return max(dfs(r,c) for r in range(n) for c in range(m))
