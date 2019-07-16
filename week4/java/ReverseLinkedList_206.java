/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        
        if (head == null || head.next == null) {
            return head;
        }
        
        // // 1st approach: recursion
        // ListNode[] root = {head};
        // reverse(head, root);
        // return root[0];
        
        // 2nd approach: iteration
        ListNode prev_node = null;
        ListNode cur_node = head;
        while (cur_node != null) {
            ListNode tmp = cur_node.next;
            cur_node.next = prev_node;
            prev_node = cur_node;
            cur_node = tmp;
        }
        
        return prev_node;
    }
    
    private ListNode reverse(ListNode head, ListNode[] root) {
        if (head.next == null) {
            root[0] = head;
            return head;
        }
        
        ListNode prev_node = reverse(head.next, root);
        prev_node.next = head;
        head.next = null;
        return head;
    }
}
