from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        # 1st approach
#         mapping = defaultdict(list)
#         count = 0
#         for word in words:
#             mapping[word[0]].append(word)
        
#         for char in S:
#             word_list = mapping[char]
#             mapping[char] = list()
            
#             for word in word_list:
#                 if len(word)==1:
#                     count+=1
#                 else:
#                     mapping[word[1]].append(word[1:])
#         return count
        
        # 2nd approach
        def isSubSeq(word: str) -> bool:
            i = 0
            for char in word:
                if i==len(S):
                    return False
                i = S.find(char,i) + 1
                if not i:
                    return False
        
            return True
        
        count = 0
        not_found = set()
        found = set()
        for word in words:
            if word in found:
                count += 1
            elif word not in not_found:
                if isSubSeq(word):
                    found.add(word)
                    count += 1
                else:
                    not_found.add(word)
        
        return count
                
