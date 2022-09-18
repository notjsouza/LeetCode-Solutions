class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            
            return list2
        
        elif not list2:
            
            return list1
        
        head = ListNode(0, None)
        ptr = head
        
        while list1 and list2:
            
            if list1.val < list2.val:
                
                head.next = list1
                list1 = list1.next
                l = True
                
            else:
                
                head.next = list2
                list2 = list2.next
                l = False
                
            head = head.next
        
        if list1:
            
            head.next = list1
            
        if list2:
            
            head.next = list2
        
        return ptr.next
