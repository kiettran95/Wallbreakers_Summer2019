class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        dict_words = dict()
        for word in A.split() + B.split():
            if word not in dict_words: 
                dict_words[word] = 1
            else: 
                dict_words[word] += 1

        return list(word for word in dict_words if dict_words[word]==1)
    
