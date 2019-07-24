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
    
    private int maxDepth = -1;
    private int leftMostValue;
    
    public int findBottomLeftValue(TreeNode root) {
        traverse(root, 0);
        return leftMostValue;
    }
    
    private void traverse(TreeNode root, int curDepth) {
        if (root == null) {
            return;
        }
        
        if (curDepth > maxDepth) {
            maxDepth = curDepth;
            leftMostValue = root.val;
        }
        
        traverse(root.left, curDepth + 1);
        traverse(root.right, curDepth + 1);
    }
}
