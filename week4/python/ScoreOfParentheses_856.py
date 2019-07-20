class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        score = 0
        for char in S:
            if char == '(':
                stack.append(score)
                score = 0
            else:
                score = max(score * 2, 1) + stack.pop()
                
        return score
