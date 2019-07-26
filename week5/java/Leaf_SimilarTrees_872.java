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
    
    private Queue<Integer> queue = new LinkedList<Integer>();
    
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        if (root1 == null || root2 == null) 
            return root1 == root2;
        
        traverse(root1, false);
        return traverse(root2, true) && queue.isEmpty();
    }
    
    private boolean traverse(TreeNode root, boolean isCheck) {
        if (root == null) return true;
        if (root.left == null && root.right == null) {
            if (isCheck) {
                return !queue.isEmpty() && queue.poll() == root.val;
            }
            queue.offer(root.val);
            return true;
        }
        return traverse(root.left, isCheck) && traverse(root.right, isCheck);
    }
}
