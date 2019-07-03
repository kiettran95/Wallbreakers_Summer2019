class Solution:            
    def findCircleNum(self, M: List[List[int]]) -> int:
        parent = {i:i for i in range(len(M))}
        
        def find(a: int) -> int:
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]

            return a
                    
        for i, a in enumerate(M):
            for j, b in enumerate(a):
                if i != j and b:
                    rootA = find(i)
                    rootB = find(j)
                    if rootA != rootB:
                        parent[rootA] = rootB
        
        res = 0
        for k,v in parent.items():
            res += 1 if k == v else 0
            
        return res