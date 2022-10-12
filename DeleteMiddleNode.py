
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        sentinal = ListNode(0, head)
        fast = slow = sentinal
        
        while fast.next and fast.next.next:
            
            fast = fast.next.next
            slow = slow.next
        
        slow.next = slow.next.next
        return sentinal.next
