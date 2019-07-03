class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 1
        new_digits = []
        for i in range(len(digits) - 1, -1, -1):    
            remainder += digits[i]
            new_digits.append(remainder % 10)
            remainder //= 10
            
        if remainder!=0:
            new_digits.append(remainder)
        
        new_digits.reverse()
        return new_digits