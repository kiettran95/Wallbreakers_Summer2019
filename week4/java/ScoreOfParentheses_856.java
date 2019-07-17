class Solution {
    public int scoreOfParentheses(String S) {
        
        Stack<Integer> stack = new Stack<>();
        // initial score
        int currentScore = 0;
        
        for (char c : S.toCharArray()) {
            if (c == '(') {
                stack.push(currentScore);
                // new score
                currentScore = 0;
            } else {
                // update current score
                currentScore = Math.max(currentScore * 2, 1) + stack.pop();
            }
        }
        return currentScore;
    }
}
