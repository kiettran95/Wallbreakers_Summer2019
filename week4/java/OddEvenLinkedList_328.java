/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode odd_node = head;
        ListNode even_node = head.next;
        ListNode root_even_node = even_node;
        
        while (even_node != null && even_node.next != null) {
            odd_node.next = even_node.next;
            odd_node = odd_node.next;
            even_node.next = odd_node.next;
            even_node = even_node.next;
        }
        odd_node.next = root_even_node;
        return head;
    }
}
