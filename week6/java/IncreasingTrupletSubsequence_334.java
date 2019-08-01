class Solution {
    public boolean increasingTriplet(int[] nums) {
        int smallestNum = Integer.MAX_VALUE;
        int midNum = Integer.MAX_VALUE;
        for (int num : nums) {
            if (smallestNum >= num) 
                smallestNum = num;
            else if (midNum >= num)
                midNum = num;
            else
                return true;
        }
        return false;
    }
}
