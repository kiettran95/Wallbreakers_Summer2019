class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) 
        if target % 2 != 0:
            return False
        
        target //= 2
        print(target)
        
        def checkPartition(cur_sum: int, index: int) -> bool:
            
            if cur_sum == target:
                return True
            
            if index < 0:
                return False
            
            for i in range(index, -1, -1):
                if cur_sum + nums[i] > target:
                    break
                
                if checkPartition(cur_sum + nums[i], i - 1):
                    return True
                
            return False
        
        return checkPartition(0, len(nums) - 1)
