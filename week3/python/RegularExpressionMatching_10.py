class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        # 1st approach: recursion
#         lenP = len(p)
#         lenS = len(s)
        
#         mem = dict()
        
#         def isEqual(a: chr, b: chr) -> bool:
#             return a == b or b == '.'
        
#         def isMatchHelper(s_index: int, p_index: int) -> bool:
#             if p_index==lenP:
#                 return s_index==len(s)
            
#             if (s_index,p_index) in mem:
#                 return mem.get((s_index,p_index))
            
#             first_match = s_index<lenS and isEqual(s[s_index],p[p_index])
            
#             if p_index<lenP-1 and p[p_index+1] == '*':
#                 res=(isMatchHelper(s_index, p_index+2)) \
#                     or first_match and isMatchHelper(s_index+1,p_index)
#             else:
#                 res=first_match and isMatchHelper(s_index+1, p_index+1)
                            
#             mem[(s_index,p_index)] = res
#             return res
            
#         return isMatchHelper(0,0)

        # 2nd approach: dynamic programming
        lenS = len(s)
        lenP = len(p)
        dp = [[False for _ in range(lenP+1)] for _ in range(lenS+1)]
        dp[0][0] = True
        for i in range(lenS+1):
            for j in range(1, lenP+1):
                if p[j-1] == '*':
                    dp[i][j] = (j >= 2) and dp[i][j-2]
                    dp[i][j] |= (i >= 1) and dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.')
                else:
                    dp[i][j] = (i >= 1) and dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                    
        return dp[-1][-1]
        
