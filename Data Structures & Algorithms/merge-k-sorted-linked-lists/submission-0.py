# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       if not lists: return None
       #performing a merge sort until we arrive at just 1 list
       while len(lists) > 1:
            res_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                res_list.append(self.merge2lists(l1, l2))
            lists = res_list
       return lists[0]
# helper func to merge 2 lists
    def merge2lists(self, list1 : ListNode, list2: ListNode):
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            elif list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next