class Solution {
    public int minMoves(int[] nums) {
        long sum = 0;
        int min_num = nums[0];
        for (int num : nums) {
            sum += num;
            min_num = Math.min(min_num, num);
        }
        return (int)(sum - min_num * nums.length);
    }
}
