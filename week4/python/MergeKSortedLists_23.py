# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
#         def mergeKLists(lists, start, end):
#             # only 1 list
#             if start == end:
#                 return lists[start]
#             # no valid list
#             if start > end:
#                 return None
            
#             mid = (start + end)//2
#             list_a = mergeKLists(lists,start, mid)
#             list_b = mergeKLists(lists,mid + 1, end)
            
#             return merge(list_a, list_b)
            
#         def merge(list_a, list_b):
#             # if list_a is empty or both list is empty, 
#             # either return list_b or empty list
#             if not list_a:
#                 return list_b
#             # if list_b is empty, return list_a
#             if not list_b:
#                 return list_a
            
#             root = cur = ListNode(-1)
#             while list_a and list_b:
#                 if list_a.val < list_b.val:
#                     cur.next = list_a
#                     list_a = list_a.next
#                 else:
#                     cur.next = list_b
#                     list_b = list_b.next
                    
#                 cur = cur.next
            
#             # append any non empty list
#             if list_a:
#                 cur.next = list_a
#             else:
#                 cur.next = list_b
                
#             return root.next
    
        # 1st approach
#         return mergeKLists(lists, 0, len(lists) - 1)
        
        # 2nd approach
        list_node = list()
        for node in lists:
            while node:
                list_node.append(node)
                node = node.next
            
        head = cur = ListNode(0)
        for node in sorted(list_node,key=lambda x:x.val):
            cur.next = node
            cur = cur.next
        
        return head.next
