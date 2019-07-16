# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        odd_node = head
        root_even_node = head.next
        even_node = root_even_node

        while even_node and even_node.next:
            odd_node.next = even_node.next
            odd_node = odd_node.next
            even_node.next =  odd_node.next
            even_node = even_node.next
            
        odd_node.next = root_even_node

        return head
        
