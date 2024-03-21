class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ''

        while head:
            s += str(head.val)
            head = head.next
        
        s = int(s, 2)

        return s
