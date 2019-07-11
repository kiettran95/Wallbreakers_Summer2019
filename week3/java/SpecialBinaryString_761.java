class Solution {
    public String makeLargestSpecial(String S) {
        StringBuilder s = new StringBuilder(S);
        PriorityQueue<String> pq = new PriorityQueue<>(Collections.reverseOrder());
        int countOne = 0;
        int j = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') countOne += 1;
            else countOne -= 1;
            
            if (countOne == 0) {
                pq.add("1" + makeLargestSpecial(s.substring(j + 1, i)) + "0");
                j = i + 1;
            }
        }
        StringBuilder result = new StringBuilder();
        while (!pq.isEmpty()) result.append(pq.remove());
        return result.toString();
    }
}
