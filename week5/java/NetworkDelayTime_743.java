class Solution {
    public int networkDelayTime(int[][] times, int N, int K) {
        List<int[]>[] graph = new ArrayList[N+1];
        for (int[] time : times) {
            if (graph[time[0]] == null)
                graph[time[0]] = new ArrayList<int[]>();
            graph[time[0]].add(new int[] {time[1], time[2]});
        }
        
        boolean[] visited = new boolean[N + 1];
        visited[K] = true;
        
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> (a[1] - b[1]));
        if (graph[K] == null)
            return -1;
        for (int[] neighbor : graph[K]) {
            heap.offer(new int[] {neighbor[0], neighbor[1]});
        }
        
        int maxDelayTime = 0;
        while (!heap.isEmpty()) {
            int[] node = heap.poll();
            if (visited[node[0]])
                continue;
            visited[node[0]] = true;
            N -= 1;
            maxDelayTime = Math.max(maxDelayTime, node[1]);
            if (graph[node[0]] == null)
                continue;
            for (int[] neighbor : graph[node[0]]) {
                if (visited[neighbor[0]])
                    continue;
                heap.offer(new int[] {neighbor[0], neighbor[1] + node[1]});
            }
        }
        return N == 1 ? maxDelayTime : -1;
    }
    
}
