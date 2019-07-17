class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        
        // 1st approach:
        // if (n == 0) {
        //     result.add("");
        // } else {
        //     for (int c = 0; c < n; c++) {
        //         for (String left : generateParenthesis(c)) {
        //             for (String right : generateParenthesis(n - 1 - c)) {
        //                 result.add("(" + left + ")" + right);
        //             }
        //         }
        //     }
        // }
        // return result;
        
        // 2nd approach:
        generate(n, n, "", result);
        return result;
    }
    
    private void generate(int left, int right, String s, List<String> result) {
        if (right < left) {
            return;
        }
        if (left == right && left == 0) {
            result.add(s);
            return;
        }
        if (left > 0) {
            generate(left - 1, right, s + "(", result);
        } 
        if (right > 0) {
            generate(left, right - 1, s + ")", result);
        }
    }
   
}
