class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # 1st approach: dynamic programming
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
            
        return max_profit
        
        # 2nd approach: recursion
#         def findMaxProfit(index: int, minPrice: int) -> int:
#             if index == len(prices):
#                 return 0
            
#             return max(prices[index]-minPrice, findMaxProfit(index+1, min(minPrice, prices[index])))
        
#         return findMaxProfit(0,prices[0])