class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor = 0
        saved=set()
        ans=0
        for index,num in enumerate(nums):
            xor^=((index+1)^num)
            if num in saved:
                ans = num
            saved.add(num)
        return [ans,xor^ans]
