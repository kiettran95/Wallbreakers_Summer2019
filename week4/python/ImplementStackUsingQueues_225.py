import queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = queue.Queue()
    

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        size = self.queue.qsize()
        self.queue.put(x)
        for _ in range(size):
            self.queue.put(self.queue.get())
        
        
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.empty():
            return self.queue.get()
        
        return -1
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.empty():
            val = self.queue.get()
            self.push(val)
            return val
        
        return -1
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
