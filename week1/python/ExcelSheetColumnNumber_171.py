class Solution:
    def titleToNumber(self, s: str) -> int:
        mul = 1
        col_num = 0
        
        for c in reversed(s):
            val = ord(c) - ord('A') + 1
            col_num += val * mul
            mul *= 26
        
        return col_num