class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s==None:
            return False
        
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
            
        return True