# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        # to set right pointer in interval of n
        while n > 0:
            n -= 1
            right = right.next
        #until right has reached null, move both left and right pointer
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
        