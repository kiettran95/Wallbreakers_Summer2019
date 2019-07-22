# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.max_diameter = 0
        def getHeight(root: TreeNode) -> int:
            if not root:
                return 0

            if not root.left and not root.right:
                return 1
            
            left_height = getHeight(root.left)
            right_height = getHeight(root.right)
            # find max diameter
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            return 1 + max(left_height, right_height)
        
        getHeight(root)
        return self.max_diameter
