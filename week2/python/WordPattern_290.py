class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(pattern)!=len(words):
            return False
        
        mapping = dict()
        seen_words = set()
        for char, word in zip(pattern, words):
            if char in mapping:
                if mapping.get(char)!=word:
                    return False
            elif word in seen_words:
                return False
            
            mapping[char] = word
            seen_words.add(word)
            
        return True
