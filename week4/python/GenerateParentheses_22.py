class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = list()
        
        def generate(count_o: int, count_c: int, paren: str):
            if count_o > count_c:
                return 

            if count_o == count_c and count_o == 0:
                result.append(paren)
                return
            
            if count_o > 0:
                generate(count_o - 1, count_c, paren + "(")
            
            if count_c > 0:
                generate(count_o, count_c - 1, paren + ")")
        
        generate(n, n, "")
        return result
