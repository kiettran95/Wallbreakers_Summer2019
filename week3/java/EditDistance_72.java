class Solution {
    public int minDistance(String word1, String word2) {
        if (word1 == null || word2 == null)
            return 0;
        
        int len1 = word1.length();
        int len2 = word2.length();
        if (len1 == 0 || len2 == 0) 
            return Math.max(len1, len2);
            
        int[] cur = new int[len2 + 1];
        for (int i = 0; i <= len2; i++) {    // Initialize with empty string case
            cur[i] = i;
        }
        
        for (char c1 : word1.toCharArray()) {
            int[] prev = cur;
            cur = new int[len2 + 1];
            cur[0] = prev[0] + 1;

            for (int i = 0; i < len2; i++) {
                char c2 = word2.charAt(i);

                if (c1 == c2) {     // If same char, update with previous count
                    cur[i + 1] = prev[i];
                    
                } else {
                    // Take min of left(delete operation), 
                    // diagonal left(shift operation) or top left (add operation)
                    cur[i + 1] = 1 + Math.min(Math.min(prev[i], prev[i + 1]), cur[i]);
                }
            }
        }
        return cur[len2];
    }
}
