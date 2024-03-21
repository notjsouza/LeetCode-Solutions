class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next: 
            return True
        
        slow, fast, pre = head.next, head.next, head

        while fast.next and fast.next.next:
            
            fast = fast.next.next

            nxt = slow.next
            slow.next = pre
            pre = slow
            slow = nxt

        if fast.next:
            slow = slow.next
        
        while pre and slow:
            if pre.val != slow.val:
                return False
            
            pre, slow = pre.next, slow.next
            
        return True
