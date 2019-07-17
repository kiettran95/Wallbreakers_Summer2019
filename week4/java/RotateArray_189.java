class Solution {
    public void rotate(int[] nums, int k) {
        
        int len = nums.length;
        k %= len;
        
        // no need to rotate
        if (k == 0) return;
        
        // cyclic moving approach
        // int count = 0;
        // for (int start = 0; count < len; start++) {
        //     int cur = start;
        //     int prev_val =  nums[cur];
        //     do {
        //         cur = (cur + k) % len;
        //         int tmp = nums[cur];
        //         nums[cur] = prev_val;
        //         prev_val = tmp;
        //         count += 1;
        //     } while (cur != start);
        // }
        
        // rotation approach
        reverse(nums, 0, len - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, len - 1);
    }
    
    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int tmp = nums[start];
            nums[start] = nums[end];
            nums[end] = tmp;
            start += 1;
            end -= 1;
        }
    }
    
}
