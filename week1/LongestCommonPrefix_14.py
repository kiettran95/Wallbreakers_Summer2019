class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        common_prefix = strs[0]
        for i in range(1, len(strs)):
            for j in range(len(common_prefix)):
                if j >= len(strs[i]):
                    common_prefix = strs[i]
                    break
                else:
                    if common_prefix[j] != strs[i][j]:
                        common_prefix = common_prefix[:j]
                        break
            
            if len(common_prefix) == 0:
                break
        
        return common_prefix