class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        sentinal = ListNode(0, head)
        slow = fast = sentinal
        i = 0
        
        while fast:
            
            if i > n:
                
                slow = slow.next
            
            fast = fast.next
            i += 1
        
        if slow.next: slow.next = slow.next.next
        else: return head.next
        
        return sentinal.next
