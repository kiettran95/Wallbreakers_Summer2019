class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l,r = 0, len(A)-1
        while l<r:
            mid = (l+r)//2
            if A[mid]<A[mid+1]:
                l = mid+1
            else:
                r = mid
        
        return l
                                
