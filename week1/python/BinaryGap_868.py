class Solution:
    def binaryGap(self, N: int) -> int:
        maxGap = 0
        count = 0
        foundOne = False
        for bit in bin(N):
            if bit == '1':
                count += 1
                if foundOne: 
                    maxGap = max(maxGap, count)
                count = 0
                foundOne = True
            else:
                count += 1
                
        return maxGap