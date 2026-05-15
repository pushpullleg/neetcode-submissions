# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       dummy = ListNode(0, head)
       groupprev = dummy

       while True:
            # find the kth node to set the start of the group
            kth = self.findkth(groupprev, k)

            if not kth: 
                break
            groupnext = kth.next

            cur = groupprev.next
             # 1st time prev should point to next group 1st element,
             # from next time, it will point to previous element within loop
            prev = kth.next
            
            while cur != groupnext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            tmp = groupprev.next
            groupprev.next = kth 
            groupprev = tmp
       return dummy.next


    def findkth(self, cur, k):
        while cur and  k > 0 :
            cur = cur.next
            k -= 1
        return cur
