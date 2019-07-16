# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # 1st approach: recursion
#         root = [head]
#         def recurse_reverse(node: ListNode) -> ListNode:
#             if not node or not node.next:
#                 root[0] = node
#                 return node

#             prev_node = recurse_reverse(node.next)
#             prev_node.next = node
#             node.next = None
#             return node
        
#         recurse_reverse(head)
#         return root[0]
    
        # 2nd approach: iteration
        if not head or not head.next:
            return head
        
        prev_node = None
        cur_node = head
        while cur_node:
            tmp = cur_node.next
            cur_node.next = prev_node
            prev_node, cur_node = cur_node, tmp
        
        return prev_node
