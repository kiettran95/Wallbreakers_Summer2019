class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) 
            return 0;
        
        // 1st approach: dynamic programming
//         int len = nums.length;
//         if (len < 4) {
//             // return Arrays.stream(nums).max().getAsInt();
//             int maxValue = 0;
//             for (int money : nums) {
//                 maxValue = Math.max(maxValue, money);
//             }
//             return maxValue;
//         }
        
//         // There are cases for any previous number of houses:
//         // 1: not take first and last
//         // 2: not take first but last
//         // 3: take first but not last
//         // 4: take first and last
//         int[] cases = {nums[1], nums[2], nums[0], nums[0] + nums[2]};
//         for (int i = 3; i < len; i++) {
//             int money = nums[i];
//             int[] tmp = {0, 0, 0, 0};
//             // not take first and last from first to current house
//             tmp[0] = Math.max(cases[0], cases[1]);
//             // not take first but last from first to current house
//             tmp[1] = cases[0] + money;
//             // take first but not last from first to current house
//             tmp[2] = Math.max(cases[2], cases[3]);
//             // take first and last from first to current house
//             tmp[3] = cases[2] + money;
            
//             // update record
//             cases = tmp;
//         }

//         int maxCase = 0;
//         for (int i = 0; i < 3; i++) {
//             maxCase = Math.max(maxCase, cases[i]);
//         }
//         return maxCase;
        
        // 2nd approach: recursion
        int not_included_first = findMax(nums, 1, nums.length);
        int included_first = findMax(nums, 0, nums.length - 1);
        return Math.max(not_included_first, included_first);
    }
    
    private int findMax(int[] nums, int start, int end) {
        if (start >= end) {
            return nums[0];
        }
        int included_prev = nums[start];
        int not_included_prev = 0;
        for (int i = start + 1; i < end; i++) {
            int tmp = included_prev;
            included_prev = Math.max(included_prev, not_included_prev + nums[i]);
            not_included_prev = tmp;
            // System.out.println("i = " + i + " a = " + included_prev + " b = " + not_included_prev);
        }
        // System.out.println(included_prev);
        // System.out.println(not_included_prev);
        return Math.max(included_prev, not_included_prev);
    }
}
