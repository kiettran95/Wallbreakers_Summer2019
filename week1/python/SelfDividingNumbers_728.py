class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        set = []
        for num in range(left, right + 1):
            tmp = num
            digit = tmp % 10
            while digit != 0 and num%digit==0:
                tmp //= 10
                digit = tmp % 10

            if tmp==0:
                set.append(num)
                
        return set