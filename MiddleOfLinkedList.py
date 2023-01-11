class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast, slow = head, head

        while fast.next and fast.next.next:

            slow = slow.next
            fast = fast.next.next
        
        return slow if not fast.next else slow.next
