class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return False
        
        countUpperChar = 0
        for c in word:
            if c.isupper():
                countUpperChar += 1
        
        return countUpperChar == 0 \
            or (countUpperChar == 1 and word[0].isupper()) \
            or (countUpperChar == len(word))