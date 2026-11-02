# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        head = ListNode()
        dummy = head
        trav_a,trav_b = a,b
        while trav_a is not None and trav_b is not None:
            if trav_a.val<trav_b.val:
                dummy.next = trav_a
                trav_a = trav_a.next
            else:
                dummy.next = trav_b
                trav_b = trav_b.next
            dummy=dummy.next
        if trav_a:
            dummy.next = trav_a
        if trav_b:
            dummy.next = trav_b
        return head.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        for i in range(1, len(lists)):
            lists[i]=self.mergeTwoLists(lists[i],lists[i-1])
        return lists[-1]
