class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        
        // 1st approach: priority queue
        // // update counter map
        // Map<Integer, Integer> counter = new HashMap<>();
        // for (int num : nums) {
        //     counter.put(num, counter.getOrDefault(num, 0) + 1);
        // }
        // // sort by frequencies with priority queue
        // PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> counter.get(b) - counter.get(a));
        // for (int num : counter.keySet()) {
        //     pq.offer(num);
        // }
        // // get k top frequencies
        // List<Integer> result = new ArrayList<>(k);
        // while (!pq.isEmpty() && k > 0) {
        //     result.add(pq.poll());
        //     k -= 1;
        // }
        // return result;
        
        // 2nd approach:
        // update counter map
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        List[] frequencies = new ArrayList[nums.length + 1];
        for (Integer num : counter.keySet()) {
            int count = counter.get(num);
            if (frequencies[count] == null) {
                frequencies[count] = new ArrayList<>();
            }
            frequencies[count].add(num);
        }
        
        List<Integer> result = new ArrayList<>();
        for (int count = nums.length; count >= 0 && result.size() < k; count--) {
            if (frequencies[count] == null) {
                continue;
            }
            Iterator<Integer> iterator = frequencies[count].iterator();
            while (iterator.hasNext() && result.size() < k) {
                result.add(iterator.next());
            }
        }
        return result;
    }
}
