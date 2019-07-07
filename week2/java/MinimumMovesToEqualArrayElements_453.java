class Solution {
    public int minMoves(int[] nums) {
        long sum = 0;
        int minNum = nums[0];
        for (int num : nums) {
            minNum = Math.min(num, minNum);
            sum += (long) num;
        }
        return (int) (sum - minNum * nums.length);
    }
}
