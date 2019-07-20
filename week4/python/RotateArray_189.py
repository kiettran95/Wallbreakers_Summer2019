class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1st approach
#         if nums:
#             k %= len(nums)
#             visited = [False]*len(nums)
#             for i in range(len(nums)):
#                 if not visited[i]:
#                     start = i
#                     tmp = nums[start]
#                     while True:
#                         visited[start] = True
#                         next_i = (start + k) % len(nums)
#                         nums[next_i], tmp = tmp, nums[next_i]

#                         if next_i == i:
#                             break
                    
#                         start = next_i
        
        # 2nd approach
        if nums:
            k %= len(nums)
            
            if k == 0:
                return
            
            nums[:] = nums[::-1]
            nums[:k] = nums[:k][::-1]
            nums[k:] = nums[k:][::-1]
