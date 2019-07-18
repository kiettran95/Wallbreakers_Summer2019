class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        
        if (k >= nums.length) return false;
        
        int max_num = 0;
        int target = 0;
        for (int num : nums) {
            target += num;
            max_num = Math.max(max_num, num);
        }
        
        if (target % k != 0 || target / k < max_num) return false;
        
        target /= k;
        boolean[] visited = new boolean[nums.length];
        return partition(nums, 0, 0, target, visited, k);
    }
    
    private boolean partition(int[] nums, int index, int cur_sum, int target, boolean[] visited, int k) {
        // base case: found all k partitions
        if (k == 0) return true;
        // current sum is not correct
        if (cur_sum > target) return false;
        // found 1 partition, continue
        if (cur_sum == target) return partition(nums, 0, 0, target, visited, k - 1);
        
        for (int i = index; i < nums.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                if (partition(nums, i + 1, cur_sum + nums[i], target, visited, k)) {
                    return true;
                }
                visited[i] = false;
            }
        }
        return false;
    }
}
