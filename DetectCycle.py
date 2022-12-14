# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dic = {}
        
        while head:
            
            if dic.get(head):
                
                return head
            
            dic[head] = True
            head = head.next
        
        return None
