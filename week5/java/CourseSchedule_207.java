class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (prerequisites == null || prerequisites.length < 2) 
            return true;

        List[] map = new ArrayList[numCourses];
        for (int[] courses : prerequisites) {
            if (map[courses[0]] == null)
                map[courses[0]] = new ArrayList<Integer>();
            map[courses[0]].add(courses[1]);
        }

        int[] groupAssigned = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if (groupAssigned[i] == 0 && !canFinish(map, i, groupAssigned))
                return false;
        }
        return true;
    }
    
    private boolean canFinish(List<Integer>[] map, int index, int[] groupAssigned) {
        if (groupAssigned[index] != 0)   
            return groupAssigned[index] == 1;
        
        groupAssigned[index] = -1;
        if (map[index] != null) {
            for (Integer course : map[index]) {
                if (!canFinish(map, course, groupAssigned))
                    return false;
            }
        }
        groupAssigned[index] = 1;
        return true;
    }
    
}
