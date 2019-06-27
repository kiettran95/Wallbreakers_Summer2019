class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def find(x: int, y: int) -> int:
            if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] == '1':
                grid[x][y] = '0'
                list(map(find, (x-1,x+1,x,x), (y,y,y-1,y+1)))
                return 1
            return 0
        
        return sum(find(i,j) for i in range(len(grid)) for j in range(len(grid[i])))