# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        l3 = dummy
        prev = None
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total =  v1 + v2 + carry

            carry = total // 10
            sum_of_2 = total % 10

            l3.next = ListNode(sum_of_2, None)
            l3 = l3.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        c = dummy.next
        while c:
            print(c.val)
            c=c.next
        return dummy.next