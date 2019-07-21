class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # 1st approach
#         result = list()
        
#         def combination(combin: List[int], index: int):
#             if len(combin) == k:
#                 result.append(list(combin))
#                 return

#             if len(combin) > k:
#                 return
            
#             for i in range(index, n + 1):
#                 combin.append(i)
#                 combination(combin, i + 1)
#                 combin[:] = combin[:-1]
                
#         combination(list(), 1)
#         return result

        # 2nd approach
        import itertools
        return list(itertools.combinations(list(range(1,n+1)),k))
