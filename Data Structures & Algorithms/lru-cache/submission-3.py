class Node:
    def __init__ (self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.first = Node(0,0)
        self.last = Node(0,0)
        self.first.next = self.last
        self.last.prev = self.first 

    def remove(self, node):
        left = node.prev
        right = node.next
        left.next,right.prev = right, left

    def insert(self, node):
        last_prev = self.last.prev
        last = self.last
        last_prev.next, last.prev = node, node
        node.next, node.prev = last, last_prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]= Node(key, value)
        self.insert(self.cache[key])
        

        if len(self.cache) > self.cap:
            lru = self.first.next
            self.remove(lru)
            del self.cache[lru.key]
            
