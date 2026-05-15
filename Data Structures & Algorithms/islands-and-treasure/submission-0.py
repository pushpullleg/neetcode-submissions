class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q, visited = deque(), set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        def addcell(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c)  in visited or grid[r][c] == -1:
                return
            q.append((r,c))
            visited.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addcell(r + 1, c)
                addcell(r, c + 1)
                addcell(r - 1, c)
                addcell(r, c - 1)
            dist += 1

