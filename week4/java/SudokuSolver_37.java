class Solution {
    public void solveSudoku(char[][] board) {
        if (board == null || board.length != 9 || board[0].length != 9) return;
        findSolution(board);
    }
    
    private boolean findSolution(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            // verify given board
            if (board[i].length != 9) return false;
            
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] != '.') continue;
                
                for (char c = '1'; c <= '9'; c++) {
                    if (!isValid(board, c, i, j)) continue;
                    
                    board[i][j] = c;
                    if (findSolution(board)) 
                        return true;
                    else 
                        board[i][j] = '.';    
                }
                return false;
            }
        }
        return true;
    }
    
    private boolean isValid(char[][] board, char c, int row, int col) {
        for (int i = 0; i < 9; i++) {
            // check row
            if (board[row][i] == c) return false;
            // check col
            if (board[i][col] == c) return false;
            // check sub square
            if (board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c) return false;
        }
        return true;
    }
}
