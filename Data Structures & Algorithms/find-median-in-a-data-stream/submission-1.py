class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -1 * num)
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -1 * heapq.heappop(self.left))
        if self.left and self.right and (-1 * self.left[0] > self.right[0]):
            heapq.heappush(self.right, -1 * heapq.heappop(self.left))
        if len(self.right) > len(self.left) + 1:
            heapq.heappush(self.left, -1 * heapq.heappop(self.right))
        #print('left:', self.left)
        #print('right:', self.right)  

    def findMedian(self) -> float:
        if len(self.right) > len(self.left):
            return self.right[0]
        if len(self.left) > len(self.right):
            return -1 * self.left[0]
        return (-1 * self.left[0] + self.right[0]) / 2
        
        