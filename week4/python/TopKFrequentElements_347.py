import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 1st approach
        # return list(zip(*collections.Counter(nums).most_common(k)))[0]
        
        # 2nd approach
        counter = dict()
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            
        counter = sorted(counter, key=lambda x:counter[x], reverse=True)
        return counter[:k]
