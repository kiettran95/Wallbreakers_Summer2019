class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        for char in set(s):
            if s.count(char)==1:
                seen.add(s.index(char))
        if seen:
            return min(seen)
        return -1
