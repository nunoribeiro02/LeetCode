/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let first = head;
    if (head == null) return head;

    while (head.next != null){
        if (first == head) {
            prev = head;
            head = head.next;
            prev.next = null;
            continue;
        }


        let cur = head;
        head = head.next;
        cur.next = prev;
        prev = cur;
    }

    if (head != first) head.next = prev;
    return head;
};