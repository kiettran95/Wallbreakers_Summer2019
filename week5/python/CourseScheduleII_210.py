class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # 1st approach: recursion topology sort ordering
        mapping = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        for [u, v] in prerequisites:
            mapping[v].append(u)
        
        def dfs(cur: int, stack: List[int]) -> bool:
            if visited[cur] == -1:
                return False
            
            if visited[cur] == 1:
                return True
            
            visited[cur] = -1
            for child in mapping[cur]:
                if not dfs(child, stack):
                    return False
            
            visited[cur] = 1
            stack.append(cur)
            return True
        
        stack = []
        for course in range(numCourses):                
            if not dfs(course, stack):
                return []
        
        return reversed(stack)
