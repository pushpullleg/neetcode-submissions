"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        oldtonew = {None:None}
        while cur:
            newCopy = Node(cur.val)
            oldtonew[cur] = newCopy
            cur = cur.next
        cur = head
        while cur:
            newCopy = oldtonew[cur]
            newCopy.next = oldtonew[cur.next]
            newCopy.random = oldtonew[cur.random]
            cur = cur.next
        return oldtonew[head]