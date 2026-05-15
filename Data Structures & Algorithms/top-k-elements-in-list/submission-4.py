class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minheap = []
        for i in count.keys():
            heapq.heappush(minheap, [count[i], i])
            if len(minheap) > k:
                heapq.heappop(minheap)
        res = []
        for j in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res