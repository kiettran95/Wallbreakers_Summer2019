class MyStack {

    private Queue<Integer> queue;
    
    /** Initialize your data structure here. */
    public MyStack() {
        queue = new LinkedList<>();
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        int size = queue.size();
        // new value is on top
        queue.offer(x);
        // update other values after new value
        while (size > 0) {
            queue.offer(queue.poll());
            size -= 1;
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        return empty() ? -1 : queue.poll();
    }
    
    /** Get the top element. */
    public int top() {
        return empty() ? -1 : queue.peek();
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return queue.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
