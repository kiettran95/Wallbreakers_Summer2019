class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
#         sums = [0]*k
#         target = sum(nums) // k
#         nums.sort(reverse=True)
#         len_nums = len(nums)
        
#         def findPartition(index: int) -> bool:

#             if index == len_nums:
#                 return len(set(sums)) == 1
            
#             for count in range(k):
#                 sums[count] += nums[index]
#                 if sums[count] <= target and findPartition(index+1):
#                     return True
                
#                 sums[count] -= nums[index]
#                 if sums[count] == 0:
#                     break
                    
#             return False        
        
#         return findPartition(0)

        target = sum(nums)
        if target % k != 0:
            return False
        
        target //= k
        len_nums = len(nums)
        visited = [False] * len_nums


        def findPartition(index: int, cur_sum: int, found: int) -> bool:
            
            if found == k:
                return True
            
            if cur_sum == target:
                return findPartition(0, 0, found + 1)
            
            for i in range(index, len(nums)):
                if visited[i] or cur_sum + nums[i] > target:
                    continue
                
                visited[i] = True
                if findPartition(i + 1, cur_sum + nums[i], found):
                    return True
                
                visited[i] = False
            
            return False
        
        return findPartition(0, 0, 0)
