# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0)
        trav = newHead
        while list1 is not None and list2 is not None:
            if list1.val<=list2.val:
                if trav is None:
                    newHead.next = list1
                    trav = list1
                else:
                    trav.next = list1
                    trav=trav.next
                list1= list1.next
            else:
                if trav is None:
                    newHead.next = list2
                    trav = list2
                else:
                    trav.next = list2
                    trav=trav.next
                list2=list2.next
        while list1 is not None:
            if trav is None:
                trav = list1
            else:
                trav.next = list1
                trav=trav.next
            list1=list1.next
        while list2 is not None:
            if trav is None:
                trav = list2
            else:
                trav.next = list2
                trav=trav.next
            list2=list2.next
        return newHead.next
                
        
        