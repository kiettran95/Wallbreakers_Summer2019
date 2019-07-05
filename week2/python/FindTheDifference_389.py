class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        saved = dict()
        for char in s:
            if char not in saved:
                saved[char]=0
            saved[char]+=1
        for char in t:
            if char not in saved or saved[char]==0:
                return char
            saved[char]-=1
        return ' '
