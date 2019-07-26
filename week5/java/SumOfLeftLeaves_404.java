/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        return sumLeft(root, false);
    }
    
    private int sumLeft(TreeNode root, boolean isLeft) {
        if (root == null)
            return 0;
        
        if (root.left == null && root.right == null) {
            if (isLeft)
                return root.val;
            return 0;
        } 
        return sumLeft(root.left, true) + sumLeft(root.right, false);
    }
}
