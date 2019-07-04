class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict()
        seen = set()
        for charS,charT in zip(s,t):
            if charS in mapping:
                if mapping.get(charS)!=charT:
                    return False
            elif charT in seen:
                return False
            mapping[charS] = charT
            seen.add(charT)
        return True
