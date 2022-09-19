# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        nxt = head
        
        while nxt.next and nxt.next.next:
            
            head = head.next
            nxt = nxt.next.next
            
        if nxt.next:
            
            return head.next
        
        return head
