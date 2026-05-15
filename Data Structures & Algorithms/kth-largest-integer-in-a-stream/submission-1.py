class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr, self.size = nums, k
        heapq.heapify(self.arr)
        # by default heap is minheap
        while len(self.arr) > self.size:
            heapq.heappop(self.arr)

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val)
        if len(self.arr) > self.size:
            heapq.heappop(self.arr)
        return self.arr[0]
        
