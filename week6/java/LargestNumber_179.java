class Solution {
    public String largestNumber(int[] nums) {
        if (nums == null || nums.length == 0)
            return "";
        
        // 1st approach
        // String[] numStr = Arrays.stream(nums).mapToObj(String::valueOf).toArray(String[]::new);
        // Arrays.sort(numStr, (s1, s2) -> (s2 + s1).compareTo(s1 + s2));
        // return Arrays.stream(numStr).reduce((x, y) -> x.equals("0") ? y : x + y).get();
        
        // 2nd approach
        String[] numStr = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            numStr[i] = String.valueOf(nums[i]);    
        }
        
        Arrays.sort(numStr, (s1, s2) -> (s2 + s1).compareTo(s1 + s2));
        
        if(numStr[0].equals("0"))
            return "0";
        
        StringBuilder stringBuilder = new StringBuilder();
        for(String str : numStr) 
            stringBuilder.append(str);
        
        return stringBuilder.toString();
    }
}
