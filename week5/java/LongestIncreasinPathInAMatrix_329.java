class Solution {
    
    private int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    public int longestIncreasingPath(int[][] matrix) {
        if (matrix == null || matrix.length == 0) 
            return 0;
        
        int[][] record = new int[matrix.length][matrix[0].length];
        int longestPath = 0;
        for (int r = 0; r < matrix.length; r++) {
            for (int c = 0; c < matrix[r].length; c++) {
                longestPath = Math.max(longestPath, findLongestPath(matrix, r, c, record));
            }
        }
        return longestPath;
    }
    
    private int findLongestPath(int[][] matrix, int r, int c, int[][] record) {
        if (record[r][c] > 0)
            return record[r][c];
        
        int longestPath = 0;
        for (int[] direction : directions) {
            int nextR = r + direction[0];
            int nextC = c + direction[1];
            if (nextR < 0 || nextC < 0 || nextR >= matrix.length 
                || nextC >= matrix[nextR].length || matrix[nextR][nextC] <= matrix[r][c]) 
                continue;
            longestPath = Math.max(longestPath, findLongestPath(matrix, nextR, nextC, record));
        }
        record[r][c] = Math.max(record[r][c], longestPath + 1);
        return 1 + longestPath;
    }
}
