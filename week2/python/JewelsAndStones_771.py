class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j_stones = set(J)
        return sum(s_stone in j_stones for s_stone in S)
        
