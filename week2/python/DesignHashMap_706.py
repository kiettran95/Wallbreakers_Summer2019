class MyNode:
        def __init__(self, key, val):
            self.key=key
            self.val=val
            self.next = None
            
class MyHashMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10
        self.arr = [None]*self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_index = hash(key)%len(self.arr)
        if not self.arr[hash_index]:
            self.arr[hash_index] = MyNode(key, value)
        else:
            node = self.arr[hash_index]
            while node.key!=key and node.next:
                node = node.next
            if node.key==key:
                node.val = value
            else:
                node.next = MyNode(key,value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_index = hash(key)%len(self.arr)
        node = self.arr[hash_index]
        while node:
            if node.key==key:
                return node.val
            node = node.next
        
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_index = hash(key)%len(self.arr)
        node = self.arr[hash_index]
        if not node:
            return -1
        if node.key == key:
            self.arr[hash_index] = node.next
        else:
            while node.next and node.next.key!=key:
                node = node.next
            if node.next:
                node.next = node.next.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
