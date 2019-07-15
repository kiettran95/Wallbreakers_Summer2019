class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        
        # 1st apprach: dynamic programming
#         # There are cases for any previous number of houses:
#         #   1: not take first and last
#         #   2: not take first but last
#         #   3: take first but not last
#         #   4: take first and last
#         cases = [nums[1], nums[2], nums[0], nums[0] + nums[2]]
#         for money in nums[3:]:
#             tmp = [0]*4
            
#             # not take first and last from first to current house
#             tmp[0] = max(cases[0],cases[1])
#             # not take first but last from first to current house
#             tmp[1] = (cases[0] + money)
#             # take first but not last from first to current house
#             tmp[2] = max(cases[2],cases[3])
#             # take first and last from from first to current house
#             tmp[3] = (cases[2] + money)

#             # update record
#             cases = tmp
            
#         return max(cases[:3])       # take max case but not the last

        # 2nd approach: recursion
        def findMax(start: int, end: int) -> int:
            included_prev = nums[start]
            not_included_prev = 0
            for i in range(start + 1, end):
                tmp = included_prev
                included_prev = max(included_prev, not_included_prev + nums[i])
                not_included_prev = tmp
            
            return max(included_prev, not_included_prev)
                
        not_included_first = findMax(1, len(nums))
        included_first = findMax(0, len(nums) - 1)
        return max(not_included_first, included_first)
            