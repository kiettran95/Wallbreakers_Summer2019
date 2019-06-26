class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [num for num in A if num % 2 == 0] + [num for num in A if num % 2 != 0]