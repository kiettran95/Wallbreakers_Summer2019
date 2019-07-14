class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1), len(word2))
            
        cur = [i for i in range(len(word2) + 1)]
        for char1 in word1:
            prev = cur
            # base case: empty string in word1
            cur = [prev[0] + 1]

            for index, char2 in enumerate(word2):
                # if equal, take previous count distance 
                if char1 == char2:
                    cur.append(prev[index])
                # else, take min of left(delete operation), 
                # diagonal left(shift operation) or top left (add operation)
                else:   
                    cur.append(min(prev[index+1],prev[index],cur[-1])+1)
                
        return cur[-1]
