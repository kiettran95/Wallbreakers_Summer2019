class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        result = [0]
        for j in range(n):
            start = len(result) - 1
            for i in range(start, -1, -1):
                result.append(result[i] | 1 << j)
                
        return result
