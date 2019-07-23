class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = dict()
        visited = dict()
        for [u,v] in prerequisites:
            if u not in mapping:
                mapping[u] = list()
                
            mapping[u].append(v)
            visited[u] = 0
            visited[v] = 0
        
        def dfs(cur: int) -> bool:
            
            if visited[cur] == -1:
                return False
        
            if cur not in mapping:
                visited[cur] = 1
            
            if visited[cur] == 1:
                return True
        
            visited[cur] = -1
            for child in mapping[cur]:
                if not dfs(child):
                    return False
            
            visited[cur] = 1
            return True
        
        for course in mapping.keys():
            if not dfs(course):
                return False
        
        return True
