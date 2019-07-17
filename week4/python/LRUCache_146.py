class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
        
        
class LRUCache:
    
    def __init__(self, capacity: int):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.record = dict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.record:
            node = self.record.get(key)
            self.updateRecord(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.record:
            node = self.record.get(key)
            node.val = value
            self.updateRecord(node)
        else:
            if self.capacity == len(self.record):
                node = self.head.next
                self.removeRecord(node)
                self.record.pop(node.key)
                
            node = Node(key,value)
            self.putRecord(node)
            self.record[key] = node
        
    def removeRecord(self, node: Node) -> None:
        left, right = node.prev, node.next
        left.next = right
        right.prev = left
        
        
    def putRecord(self, node: Node) -> None:
        left, right = self.tail.prev, self.tail
        left.next = node
        node.prev = left
        right.prev = node
        node.next = right
        
        
    def updateRecord(self, node: Node) -> None:
        self.removeRecord(node)
        self.putRecord(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
