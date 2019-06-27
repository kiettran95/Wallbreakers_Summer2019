class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i,num in enumerate(nums):
            if (target-num) in d:
                return [d.get(target-num), i]
            else:
                d[num] = i
        return [-1, -1]
                