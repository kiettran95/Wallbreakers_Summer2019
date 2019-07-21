class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        length = len(board)
        rows = [0] * len(board)
        cols = [0] * len(board)
        squares = [0] * len(board)
        
        def isValid(x: int, y: int, num: str) -> bool:
            # 1st approach
            # check by iterations
#             for i in range(len(board)):
#                 if board[i][y] == num:
#                     return False
#                 if board[x][i] == num:
#                     return False
#                 if board[3 * (x // 3) + i // 3][3 * (y // 3) + i % 3] == num:
#                     return False
            
#             return True

            # 2nd approach
            # check by recording in bits
            mark = 1<<int(num)
            return (not bool(rows[x] & mark)) \
                    and (not bool(cols[y] & mark)) \
                    and (not bool(squares[3*(x//3) + y//3] & mark))
        
        
        def solve(r: int, c: int) -> bool:
            if r >= length:
                return True
            
            if c >= length:
                return solve(r + 1, 0)
            
            # check next if not a space
            if board[r][c] != '.':
                return solve(r, c + 1)            

            for z in range(1, 10):
                num = str(z)
                if not isValid(r, c, num):
                    continue

                board[r][c] = str(num)
                mark = 1<<int(board[r][c])
                rows[r] |= mark
                cols[c] |= mark
                squares[3*(r//3) + c//3] |= mark
                
                if solve(r, c + 1):
                    return True
                
                board[r][c] = '.'
                rows[r] ^= mark
                cols[c] ^= mark
                squares[3*(r//3) + c//3] ^= mark

            return False
                    
        for r in range(length):
            for c in range(length):
                if board[r][c] == '.':
                    continue
                
                mark = 1<<int(board[r][c])
                rows[r] |= mark
                cols[c] |= mark
                squares[3*(r//3) + c//3] |= mark
                
        solve(0,0)
