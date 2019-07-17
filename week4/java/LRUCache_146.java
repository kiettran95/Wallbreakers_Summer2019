class LRUCache {

    class Node {
        int key;
        int val;
        Node next, prev;
        Node(int _key, int _val) {
            key = _key;
            val = _val;
        }
    }
    
    private Node head, tail;
    private int maxCapacity;
    private Map<Integer, Node> record;
    
    public LRUCache(int capacity) {
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head.next = tail;
        tail.prev = head;
        maxCapacity = capacity;
        record = new HashMap<>();
    }
    
    public int get(int key) {
        int value = -1;
        if (record.containsKey(key)) {
            Node node = record.get(key);
            updateRecord(node);
            value = node.val;
        }
        return value;
    }
    
    public void put(int key, int value) {
        if (record.containsKey(key)) {
            Node node = record.get(key);
            node.val = value;
            updateRecord(node);
        } else {
            if (maxCapacity == 0) {
                return;
                
            } else if (maxCapacity <= record.size()) {
                record.remove(tail.prev.key);
                removeRecord(tail.prev);
            }
            
            Node newNode = new Node(key, value);
            putRecord(newNode);
        }
    }
    
    private Node removeRecord(Node removedNode) {
        removedNode.prev.next = removedNode.next;
        removedNode.next.prev = removedNode.prev;
        removedNode.next = null;
        removedNode.prev = null;
        return removedNode;
    }
    
    private void putRecord(Node node) {
        head.next.prev = node;
        node.next = head.next;
        node.prev = head;
        head.next = node;
        record.put(node.key, node);
    }
    
    private void updateRecord(Node node) {
        removeRecord(node);
        putRecord(node);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
