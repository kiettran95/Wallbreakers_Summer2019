class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        found = set()
        result = list()
        
        i = 0
        while i<len(S):
            found.add(S[i])
            # find all char in range
            start,end = i,S.rfind(S[i])
            while i <= end:
                # update end range
                if S[i] not in found:
                    found.add(S[i])
                    end = max(end, S.rfind(S[i]))
                i+=1
                
            # add new range
            result.append(end - start + 1)
                
        return result
