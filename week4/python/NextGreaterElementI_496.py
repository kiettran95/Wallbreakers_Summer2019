class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping = dict()
        for num in nums2:
            while stack and stack[-1] < num:
                mapping[stack.pop()] = num
            stack.append(num)
            
        result = []
        for num in nums1:
            result.append(mapping[num] if num in mapping else -1)
        
        return result
            
