class Solution {
    
    private int index;
    
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] prerequisite : prerequisites) {
            graph.putIfAbsent(prerequisite[0], new ArrayList<Integer>());
            graph.get(prerequisite[0]).add(prerequisite[1]);
        }
        
        int[] orderedCourses = new int[numCourses];
        int[] visited = new int[numCourses];
        
        for (int i = 0; i < numCourses; i++) {
            if (!topologicalSort(graph, visited, orderedCourses, i)) 
                return new int[0];
        }
        return orderedCourses;
    }
    
    private boolean topologicalSort(Map<Integer, List<Integer>> graph, int[] visited, int[] orderedCourses, int course) {
        if (visited[course] != 0)
            return visited[course] == 1;
        
        visited[course] = -1;
        if (graph.containsKey(course)) {
            for (Integer prerequisite : graph.get(course)) {
                if (!topologicalSort(graph, visited, orderedCourses, prerequisite)) 
                    return false;
            }
        }
        orderedCourses[index++] = course;
        visited[course] = 1;
        return true;
    }
}
