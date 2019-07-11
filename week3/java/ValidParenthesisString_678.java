class Solution {
    public boolean checkValidString(String s) {
        int closeParen = 0;
        int openParen = 0;
        for (char c : s.toCharArray()) {
            openParen += c == '(' ? 1 : -1;
            closeParen += c != ')' ? 1 : -1;
            if (closeParen < 0) break;
            openParen = Math.max(0, openParen);
        }
        return openParen == 0;
    }
}
