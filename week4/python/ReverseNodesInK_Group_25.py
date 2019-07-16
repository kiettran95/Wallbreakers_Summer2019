# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        node = head
        stack = []
        for _ in range(k):
            if not node:
                break
                
            stack.append(node)
            node = node.next
        
        if len(stack) == k:
            head_group = stack.pop()
            cur = head_group

            while stack:
                cur.next = stack.pop()
                cur = cur.next
            
            cur.next = self.reverseKGroup(node, k)
            
        else:
            head_group = stack[0] if stack else None
            
        return head_group
                
