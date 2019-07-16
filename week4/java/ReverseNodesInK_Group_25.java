/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode cur = head;
        int count = 0;
        while (cur != null && count < k) {
            count += 1;
            cur = cur.next;
        }
        if (count == k) {
            ListNode prev = null;
            ListNode lastNode = head;
            while (count > 0) {
                ListNode tmp = head.next;
                head.next = prev;
                prev = head;
                head = tmp;
                count -= 1;
            }
            lastNode.next = reverseKGroup(cur, k);
            return prev;
        }
        return head;
    }
}
