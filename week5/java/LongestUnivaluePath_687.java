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
    
    private int maxPath;
    public int longestUnivaluePath(TreeNode root) {
        // int[] maxPath = new int[1];
        findMaxDepth(root);
        return maxPath;
    }
    
    private int findMaxDepth(TreeNode root) {
        if (root == null || (root.left == null && root.right == null)) {
            return 0;
        }
        
        // find max left Univalue depth and record it if same value
        int leftUnivalueDepth = findMaxDepth(root.left) + 1;
        // find max right Univalue depth and record it if same value
        int rightUnivalueDepth = findMaxDepth(root.right) + 1;
        
        int maxCurDepth = 0;
        // int curPath = 0;
        
//         if (root.left != null && root.left.val == root.val) {
//             curPath = leftUnivalueDepth;
//             maxCurDepth = leftUnivalueDepth;
//         } 
        
//         if (root.right != null && root.right.val == root.val) {
//             curPath += rightUnivalueDepth;
//             maxCurDepth = Math.max(maxCurDepth, rightUnivalueDepth);
//         }
        
        if (root.left != null && root.left.val == root.val) {
            if (root.right != null && root.right.val == root.val) {
                maxPath = Math.max(maxPath, leftUnivalueDepth + rightUnivalueDepth);
                maxCurDepth = Math.max(leftUnivalueDepth, rightUnivalueDepth);
            } else {
                maxCurDepth = leftUnivalueDepth;
                maxPath = Math.max(maxPath, leftUnivalueDepth);
            }
            
        } else if (root.right != null && root.right.val == root.val) {
            maxPath = Math.max(maxPath, rightUnivalueDepth);
            maxCurDepth = rightUnivalueDepth;
        }
        
        // update found maxPath
        // maxPath = Math.max(maxPath, curPath);
        
        return maxCurDepth;
    }
}
