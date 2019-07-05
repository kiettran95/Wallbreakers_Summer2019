class Solution:
    def frequencySort(self, s: str) -> str:
        saved=dict()
        for char in s:
            if char not in saved:
                saved[char]=0
            saved[char]+=1
        ans=""
        for char,count in sorted(saved.items(), key=lambda x: x[1], reverse = True):
            while count>0:
                ans+=char
                count-=1
        return ans
