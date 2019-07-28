class Solution {
    public boolean exist(char[][] board, String word) {
        if (word == null || word.length() == 0 || board == null || board.length == 0)
            return true;
        
        boolean[][] visited = new boolean[board.length][board[0].length];
        char[] charArr = word.toCharArray();
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (isWordExist(board, charArr, i, j, 0, visited))
                    return true;
            }
        }
        return false;
    }
    
    private boolean isWordExist(char[][] board, char[] charArr, int r, int c, int index, boolean[][] visited) {
        if (index == charArr.length)
            return true;
        
        if (r < 0 || c < 0 || r >= board.length || c >= board[r].length || board[r][c] != charArr[index] || visited[r][c])
            return false;
        
        index += 1;
        visited[r][c] = true;
        boolean found =  isWordExist(board, charArr, r + 1, c, index, visited)
                        || isWordExist(board, charArr, r, c + 1, index, visited)
                        || isWordExist(board, charArr, r - 1, c, index, visited)
                        || isWordExist(board, charArr, r, c - 1, index, visited);
        visited[r][c] = false;
        return found;
    }
    
}
