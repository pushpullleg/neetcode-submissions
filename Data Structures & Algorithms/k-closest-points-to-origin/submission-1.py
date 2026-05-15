class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        res = []
        for x, y in points:
            minheap.append([x**2 + y**2, x, y])
        heapq.heapify(minheap)
        print(minheap)
        while k > 0:
            dist, x, y = heapq.heappop(minheap)
            k -= 1
            res.append([x, y])
        return res