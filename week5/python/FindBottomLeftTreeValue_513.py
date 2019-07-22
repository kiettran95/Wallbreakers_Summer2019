# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        # 1st approach: recursion
#         self.max_depth = -1
#         self.left_most = -1
#         def traverse(root: TreeNode, cur_depth: int):
#             if not root:
#                 return 

#             if not root.left and not root.right:
#                 if cur_depth > self.max_depth:
#                     self.left_most = root.val
#                     self.max_depth = cur_depth
                    
#             traverse(root.left, cur_depth + 1)    
#             traverse(root.right, cur_depth + 1)
        
#         traverse(root, 0)
#         return self.left_most

        # 2nd approach: iteration
        import collections
        queue = collections.deque()
        queue.append((root, 0))
        max_depth = -1
        left_most = -1
        while queue:
            node, cur_depth = queue.popleft()
            if cur_depth > max_depth:
                left_most = node.val
                max_depth = cur_depth
            
            if node.left:
                queue.append((node.left, cur_depth + 1))
                
            if node.right:
                queue.append((node.right, cur_depth + 1))
        
        return left_most
