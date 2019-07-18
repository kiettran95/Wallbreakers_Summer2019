class Solution {
    public boolean canPartition(int[] nums) {
        int target = 0;
        for (int num : nums) {
            target += num;
        }
        
        if ((target & 1) == 1) return false;
        
        target /= 2;
        int len = nums.length;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        
        for (int num : nums) {
            boolean[] prev = dp;
            dp = new boolean[target + 1];
            dp[0] = true;
            for (int j = 1; j <= target; j++) {
                if (num > j) continue;
                dp[j] = prev[j] | prev[j - num];
            }
            if (dp[target]) return true;
        }
        return dp[target];
    }
}
