class Solution {
    private Random rand = new Random();
    public int minMoves2(int[] nums) {
        int n = nums.length;
        int mid = n / 2;
        
        // Get middle num
        // TODO: quickSelect
        Arrays.sort(nums);
        // int target = nums[mid];
        

        int numMove = 0;
        // for (int num : nums) {
        //     numMove += Math.abs(target - num);
        // }
        
        int l = 0;
        int r = n - 1;
        while (l < r) {
            numMove += nums[r] - nums[l];
            r -= 1;
            l += 1;
        }
        return numMove;
    }
    
    // private void swap(int[] nums, int l, int r) {
    //     int tmp = nums[l];
    //     nums[l] = nums[r];
    //     nums[r] = tmp;
    // }
}
