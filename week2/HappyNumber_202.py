class Solution:
    def isHappy(self, n: int) -> bool:
        saved_nums = set()
        while n != 1:
            saved_nums.add(n)
            new_n = 0
            while n != 0:
                new_n += (n%10)**2
                n//=10
            
            if new_n in saved_nums:
                return False
            n = new_n
            
        return True
