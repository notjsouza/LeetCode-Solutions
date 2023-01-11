class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        d = {}

        while head:

            if d.get(head): return head
            d[head] = True
            head = head.next

        return None
