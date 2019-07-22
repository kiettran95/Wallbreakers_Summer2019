# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        leaf_sequence = list()
        def traverse(root: TreeNode, found: bool):
            if not root:
                return True
            
            if not root.left and not root.right:
                if found:
                    if leaf_sequence[0] != root.val:
                        return False
                    leaf_sequence[:] = leaf_sequence[1:]
                else:
                    leaf_sequence.append(root.val)
                return True
            
            return traverse(root.left, found) \
                    and traverse(root.right, found)
            
        traverse(root1, False)
        return traverse(root2, True)
