class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        combine(n, k, 1, new ArrayList<Integer>(k), result);
        return result;
    }
    
    private void combine(int n, int k, int start, List<Integer> list, List<List<Integer>> result) {
        if (k == 0) {
            result.add(new ArrayList<Integer>(list));
            return;
        }
        
        for (int i = start; i <= n - k + 1; i++) {
            list.add(i);
            combine(n, k - 1, i + 1, list, result);
            list.remove(list.size() - 1);
        }
    }
}
