class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = list()
        candidates = sorted(candidates, reverse=True)
        
        def combination(cur_list: List[int], cur_sum: int, index: int):
            if index < 0 or cur_sum > target:
                return
            
            if cur_sum == target:
                result.append(list(cur_list))
            
            for i in range(index, -1, -1):
                if cur_sum + candidates[i] > target:
                    break
                    
                cur_list.append(candidates[i])
                combination(cur_list, cur_sum + candidates[i], i)
                cur_list[:] = cur_list[:-1]
                
        combination(list(), 0, len(candidates) - 1)
        return result
