class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        terminal = ListNode(0, None)
        ptr = terminal

        while list1 and list2:

            if list1.val <= list2.val: 
                ptr.next = list1
                list1 = list1.next

            else:
                ptr.next = list2
                list2 = list2.next

            ptr = ptr.next

        if list1: ptr.next = list1
        else: ptr.next = list2

        return terminal.next
