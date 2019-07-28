class Solution {
    public boolean isBipartite(int[][] graph) {
        if (graph == null || graph.length < 2)
            return true;
        
        int[] colors = new int[graph.length];
        for (int i = 0; i < graph.length; i++) {
            if (colors[i] != 0)
                continue;
            if (!colorGraph(graph, i, 1, colors))
                return false;
        }
        return true;
    }
    
    private boolean colorGraph(int[][] graph, int index, int color, int[] colors) {
        if (colors[index] != 0)
            return colors[index] == color;
        
        colors[index] = color;
        for (int i : graph[index]) {
            if (!colorGraph(graph, i, -color, colors))
                return false;
        }
        return true;
    }
}
