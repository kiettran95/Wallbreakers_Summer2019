class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def subset(index: int, cur: List[int]):
            
            result.append(list(cur))
            if index >= len(nums):
                return
            
            for i in range(index, len(nums), 1):
                cur.append(nums[i])
                subset(i + 1, cur)
                cur[:] = cur[:-1]
                
        subset(0, list())
        
        return result
