class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int[] counter = new int[1001];
        for (int num : arr1)
            counter[num] += 1;
        
        int index = 0;
        for (int num : arr2) {
            while (counter[num]-- > 0) 
                arr1[index++] = num;
        }
        for (int i = 0; i < counter.length; i++) {
            while (counter[i]-- > 0) {
                arr1[index++] = i;
            }
        }
        return arr1;
    }
}
