# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        trav, reverse = head, newHead
        while trav is not None:
            nextNode = trav.next
            trav.next =  reverse
            reverse = trav
            trav = nextNode
        return reverse