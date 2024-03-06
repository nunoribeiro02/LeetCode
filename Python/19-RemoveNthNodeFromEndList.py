# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newHead = ListNode(val=0, next=head)
        cur = newHead
        node = newHead
        i = 0

        while (cur != None):
            cur = cur.next
            i += 1

            # To keep a distance of n+1 between pointers
            if (i > n+1): 
                node = node.next
        
        node.next = node.next.next
        return newHead.next

# Time complexity: O(n)
# Space complexity: O(1)