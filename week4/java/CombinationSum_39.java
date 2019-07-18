class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<>();
        combination(candidates, 0, target, new ArrayList<Integer>(), result);
        return result;
    }
    
    private void combination(int[] candidates, int index, int target, List<Integer> list, List<List<Integer>> result) {
        
        if (target < 0) return;
        
        if (target == 0) {
            result.add(new ArrayList<Integer>(list));
        }
        
        for (int i = index; i < candidates.length; i++) {
            int tmp = target - candidates[i];
            
            if (tmp < 0) continue;
            
            list.add(candidates[i]);
            
            if (tmp == 0) {
                result.add(new ArrayList<>(list));
            } else {
                combination(candidates, i, tmp, list, result);
            }
            list.remove(list.size() - 1);
        }
    }
}
