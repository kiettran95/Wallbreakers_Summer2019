class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        mid_len_s = len_s // 2
        
        for i in range(0,mid_len_s):
            tmp = s[i]
            s[i] = s[len_s-i-1]
            s[len_s-i-1] = tmp