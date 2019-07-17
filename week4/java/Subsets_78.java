class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        subsets(nums, 0, new ArrayList<Integer>(), result);
        return result;
    }
    
    private void subsets(int[] nums, int start, List<Integer> list, List<List<Integer>> result) {
        
        result.add(new ArrayList<>(list));
        if (start >= nums.length) {
            return;
        }
        
        for (int i = start; i < nums.length; i++) {
            list.add(nums[i]);
            subsets(nums, i + 1, list, result);
            list.remove(list.size() - 1);
        }
    }
    
}
