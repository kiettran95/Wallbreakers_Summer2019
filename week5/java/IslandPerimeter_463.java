class Solution {
    public int islandPerimeter(int[][] grid) {

        int diameter = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                int cell = grid[r][c];
                if (cell == 0) continue;

                diameter += 4;
                if (c < grid[0].length - 1 && grid[r][c + 1] == cell)
                    diameter -= 2;
                if (r < grid.length - 1 && grid[r + 1][c] == cell)
                    diameter -= 2;
            }   
        }
        return diameter;
    }
}
