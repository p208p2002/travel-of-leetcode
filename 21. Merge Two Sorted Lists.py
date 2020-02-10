# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(l1 is None and l2 is None):
            return None
        
        l3_head = ListNode(0)
        l3 = l3_head
        while(1):
            if(l1 is not None and l2 is not None):
                if(l1.val > l2.val):
                    l3.val = l2.val
                    l2 = l2.next
                else:
                    l3.val = l1.val
                    l1 = l1.next
            elif(l2 is not None):
                l3.val = l2.val
                l2 = l2.next
            elif(l1 is not None):
                l3.val = l1.val
                l1 = l1.next
            else:
                break
            
            #
            if(l1 is None and l2 is None):
                break
            
            #
            l3.next = ListNode(0)
            l3 = l3.next
            
        return l3_head
