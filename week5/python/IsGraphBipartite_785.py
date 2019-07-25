class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        # colors = [0] * len(graph)
        colors = dict()
        def dfs(node: int, color: int) -> bool:
            if node in colors:
                return colors[node] == color
            colors[node] = color
            for child in graph[node]:
                if not dfs(child, -color):
                    return False
                    
            return True
        
        for node in range(len(graph)):
            if node not in colors and not dfs(node, 1):
                return False
            
        return True
