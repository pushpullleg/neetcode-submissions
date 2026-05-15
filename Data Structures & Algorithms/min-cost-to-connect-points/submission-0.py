class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        size = len(points)
        adj = defaultdict(list)
        for i in range(size):
            xi, yi = points[i]
            for j in range(i + 1, size):
                xj, yj = points[j]
                cost = abs(xi - xj) + abs(yi - yj)
                adj[i].append((cost, j))
                adj[j].append((cost, i))
        res = 0
        minH = [(0, 0)]
        visited = set()
        while len(visited) < size:
            cost, node = heapq.heappop(minH)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for c, n in adj[node]:
                heapq.heappush(minH, (c, n))
        return res