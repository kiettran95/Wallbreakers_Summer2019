class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        # 1st approach:
#         num_cells = 0
#         neighbors = 0
#         for row in range(len(grid)):
#             for col in range(len(grid[0])):
#                 if not grid[row][col]:
#                     continue
#                 num_cells +=j 1
#                 if (row+1 < len(grid) and grid[row+1][col]):
#                     neighbors += 1
#                 if (col+1 < len(grid[0]) and grid[row][col+1]):
#                     neighbors += 1
                    
#         return num_cells*4 - neighbors*2

        # 2nd approach
        return sum(sum(map(operator.ne, [0] + row, row + [0]))
               for row in grid + list(map(list, zip(*grid))))
