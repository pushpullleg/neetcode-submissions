class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = Counter(tasks)
        minheap = [-i for i in frequency.values()]
        heapq.heapify(minheap)
        d = deque()
        time = 0
        while minheap or d:
            time += 1
            if minheap:
                popped = heapq.heappop(minheap)
                if popped + 1:
                    d.append([popped + 1, time + n])
            if d and d[0][1] == time:
                heapq.heappush(minheap, d.popleft()[0])
        return time
        