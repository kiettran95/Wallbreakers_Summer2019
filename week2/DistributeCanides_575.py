class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        # candies_set = set(candies)
        return len(candies)//2 if len(candies)//2 < len(set(candies)) else len(set(candies))
