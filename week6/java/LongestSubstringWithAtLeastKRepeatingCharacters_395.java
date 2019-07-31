class Solution {
    public int longestSubstring(String s, int k) {
        
        char[] charArr = s.toCharArray();
        int longestLength = 0, lenS = charArr.length, limitM = Math.min(27, Math.max(lenS, 2));
        
        for (int m = 0; m < limitM; m++) {
            int[] counter = new int[26];
            int start = 0, end = 0, numUniqueChars = 0, numCountMoreThanK = 0;
             
            while (end < lenS) {
                if (numUniqueChars <= m) {
                    int index = charArr[end] - 'a';
                    if (counter[index] == 0)
                        numUniqueChars += 1;
                    
                    counter[index] += 1;
                    if (counter[index] == k) 
                        numCountMoreThanK += 1;
                    
                    end += 1;
                } else {
                    int index = charArr[start] - 'a';
                    if (counter[index] == 1)
                        numUniqueChars -= 1;
                    
                    if (counter[index] == k)
                        numCountMoreThanK -= 1;
                    
                    counter[index] -= 1;
                    start += 1;
                }
                
                if (numUniqueChars == m && numCountMoreThanK == m) {
                    longestLength = Math.max(longestLength, end - start);
                }
            }
        }
        return longestLength;
    }
}
