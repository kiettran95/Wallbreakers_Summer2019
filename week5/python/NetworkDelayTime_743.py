class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        network = collections.defaultdict(list)
        for u,v,w in times:
            network[u].append((v,w))
        
        distances = dict()
        pq = [(0,K)]
        while pq:
            distance, node = heapq.heappop(pq)
            if node in distances:
                continue
            distances[node] = distance
            for neighbor, dist in network[node]:
                if neighbor not in distances:
                    heapq.heappush(pq,(distance+dist,neighbor))
            
        return max(distances.values()) if len(distances)==N else -1
