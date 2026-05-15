class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge = defaultdict(list)
        minheap = [(0, k)]
        minDist = 0
        for u, v, t in times:
            edge[u].append((v, t))
        visited = set()
        while minheap:
            dist, node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            minDist = dist
            for adj, time in edge[node]:
                if adj not in visited:
                    heapq.heappush(minheap, (time + dist, adj))
        return minDist if len(visited) == n else -1