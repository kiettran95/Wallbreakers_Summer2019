class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s = sorted(s)
        s_i = len(s) - 1
        count = 0
        
        for factor_g in sorted(g, reverse=True):
            if s_i < 0:
                return count
            
            if s[s_i]>=factor_g:
                count += 1
                s_i -= 1
        
        return count
