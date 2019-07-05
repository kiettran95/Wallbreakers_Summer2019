class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans = ""
        set_words = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                isGood = True
                for i in range(1, len(word)):
                    if word[:i] not in set_words:
                        isGood = False
                        break
                
                if isGood:
                    ans = word

        return ans
