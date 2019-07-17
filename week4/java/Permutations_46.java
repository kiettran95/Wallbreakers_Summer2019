class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        permute(nums, new ArrayList<Integer>(), result);
        return result;
    }
    
    private void permute(int[] nums, List<Integer> list, List<List<Integer>> result) {
        if (list.size() == nums.length) {
            result.add(new ArrayList<Integer>(list));
            return;
        }
        for (int num : nums) {
            if (list.contains(num)) continue;
            list.add(num);
            permute(nums, list, result);
            list.remove(list.size() - 1);
        }
    }
}
