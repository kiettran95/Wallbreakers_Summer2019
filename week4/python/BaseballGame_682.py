class Solution:
    def calPoints(self, ops: List[str]) -> int:
        point = 0
        stack = []
        for s in ops:
            if s == 'C':
                point -= stack.pop()
            elif s == 'D':
                stack.append(stack[-1]*2)
                point += stack[-1]
            elif s == '+':
                stack.append(stack[-1] + stack[-2])
                point += stack[-1]
            else:
                stack.append(int(s))
                point += stack[-1]
        
        return point
