# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        self.left_sum = 0
        def traverse(node: TreeNode, isLeft: bool):
            if not node:
                return
            
            if not node.left and not node.right:
                if isLeft:
                    self.left_sum += node.val
                return
            
            traverse(node.left, True)
            traverse(node.right, False)
        
        traverse(root, False)
        return self.left_sum
