# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        
        self.max_path = 0
        def getPath(root: TreeNode) -> int:
            if not root:
                return 0
            
            if not root.left and not root.right:
                return 1
            
            cur_path = 0
            max_height = 0
            if root.left:
                height = getPath(root.left)
                if root.val == root.left.val:
                    cur_path += height
                    max_height = height
            
            if root.right:
                height = getPath(root.right)
                if root.val == root.right.val:
                    cur_path += height
                    max_height = max(max_height, height)
            
            self.max_path = max(self.max_path, cur_path)
            return 1 + max_height
        
        getPath(root)
        return self.max_path
