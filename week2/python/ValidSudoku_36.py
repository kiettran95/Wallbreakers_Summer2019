class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_groups = set()
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num=='.': 
                    continue
                for group in ((row,num),(num,col),(row//3,col//3,num)):
                    if group in check_groups: 
                        return False
                    check_groups.add(group)
                    
        return True
