class Solution {
    public List<Integer> grayCode(int n) {
        
        // 1st approach
        // List<Integer> result = new ArrayList<>();
        // result.add(0);
        // for (int i = 0; i < n; i++) {
        //     int current_size = result.size();
        //     for (int j = current_size - 1; j >= 0; j--) {
        //         int value = (1 << i) | result.get(j); 
        //         result.add(value);
        //     }
        // }
        // return result;
        
        // 2nd approach
        List<Integer> result = new ArrayList<>();
        int size = 1 << n;
        for (int i = 0; i < size; i++) {
            result.add(i ^ i>>1);
        }
        return result;
    }
}
