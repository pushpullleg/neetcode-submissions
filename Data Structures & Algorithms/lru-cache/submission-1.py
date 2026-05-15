class Node:
    def __init__(self, key, val):
        # define the node with 4 values, key val and prev and next pointer
        self.key , self.val = key, val
        self.prev = self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.first, self.last = Node(0,0), Node(0,0)
        # link them to each other at start
        self.first.next , self.last.prev = self.last, self.first
    
    def remove(self, node):
        left, right = node.prev, node.next
        left.next, right.prev = right, left

    def insert(self, node):
        left, right = self.last.prev, self.last
        left.next = right.prev = node
        node.prev, node.next = left, right

    def get(self, key: int) -> int:
        # when you get, push it to Most Recently Used
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)    
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.first.next
            self.remove(lru)
            del self.cache[lru.key]
        
