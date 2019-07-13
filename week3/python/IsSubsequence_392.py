class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): 
            return False
        
        s_index = 0
        for char in t:
            if s_index == len(s):
                return True
            
            if char == s[s_index]:
                s_index += 1
        
        return s_index == len(s)
