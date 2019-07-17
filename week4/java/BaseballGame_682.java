class Solution {
    public int calPoints(String[] ops) {
        
        Stack<Integer> stack = new Stack<>();
        
        for (String num : ops) {
            if (num.equals("C")) {
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            } else if (num.equals("D")) {
                if (!stack.isEmpty()) {
                    int last_value = stack.peek();
                    // add double last value
                    stack.push(2 * last_value);
                }
            } else if (num.equals("+") && stack.size() > 1) {
                int last_value = stack.pop();
                int prev_last_value = stack.peek();
                // push back last value
                stack.push(last_value);
                // push sum last 2 values
                stack.push(last_value + prev_last_value);
            } else {
                int value = Integer.parseInt(num);
                // push new value
                stack.push(value);
            }
        }
        // get sum of all values
        int sum = 0;
        while (!stack.isEmpty()) {
            sum += stack.pop();
        }
        return sum;
    }
}
