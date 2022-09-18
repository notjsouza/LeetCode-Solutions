class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        pre = None
        
        while head:
            
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
            
        return pre
