class Solution {
    public void duplicateZeros(int[] arr) {
        if (arr == null || arr.length == 0)
            return;
        
        int lenArr = arr.length;
        int numZero = 0;
        int i = 0;
        
        for (; i + numZero < lenArr; i++) {
            numZero += arr[i] == 0 ? 1 : 0;
        }
        
        for (i -= 1; numZero > 0; i--) {
            if (i + numZero < lenArr) 
                arr[i + numZero] = arr[i];
            
            if (arr[i] == 0) 
                arr[i + --numZero] = arr[i];
        }
    }
}
