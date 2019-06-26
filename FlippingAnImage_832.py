class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[(num+1)%2 for num in reversed(A[i])] for i in range(len(A))]