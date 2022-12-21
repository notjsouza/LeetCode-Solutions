class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow, fast = head, head

        while fast.next and fast.next.next:

            fast = fast.next.next
            slow = slow.next
        
        return slow if not fast.next else slow.next
