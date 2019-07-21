class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = list()
        
        def permutation(pemur: List[int], visited: List[int]):
            if len(pemur) == len(nums):
                result.append(list(pemur))
                return
            
            for i in range(len(nums)):
                num = nums[i]
                if not visited[i]:
                    visited[i] = True
                    pemur.append(num)
                    permutation(pemur, visited)
                    visited[i] = False
                    pemur[:] = pemur[:-1]
        

        permutation(list(), [False] * len(nums))
        return result
