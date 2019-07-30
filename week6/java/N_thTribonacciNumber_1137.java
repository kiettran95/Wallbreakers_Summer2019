class Solution {
    public int tribonacci(int n) {
        if (n == 0)
            return 0;
        if (n < 3)
            return 1;
        int a = 0, b = 1, c = 1;
        for (; n > 2; n--) {
            int tmp = a + b + c;
            a = b;
            b = c;
            c = tmp;
        }
        return c;
    }
}
