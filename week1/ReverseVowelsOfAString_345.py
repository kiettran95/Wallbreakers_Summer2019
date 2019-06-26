class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        
        s_list = list(s)
        vowels = set('aeiouAEIOU')
        l, r = 0, len(s)-1
        while l < r:
            while l <= r and s_list[l] not in vowels: l += 1
            while l <= r and s_list[r] not in vowels: r -= 1
            if l > r: 
                break
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l, r = l + 1, r - 1
            
        return ''.join(s_list)
