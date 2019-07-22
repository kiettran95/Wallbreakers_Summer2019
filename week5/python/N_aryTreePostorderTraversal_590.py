"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        result = list()
        # 1st approach: recursion
#         def traverse(root: 'Node'):
#             if not root:
#                 return root
            
#             for node in root.children:
#                 traverse(node)
            
#             result.append(root.val)
        
#         traverse(root)
#         return result

        # 2nd approach: iteration
        if not root:
            return list()
        
        stack = [root]
        while stack:
            node = stack.pop()
            for child in node.children:
                if child:
                    stack.append(child)
            result.append(node.val)
        
        return result[::-1]
