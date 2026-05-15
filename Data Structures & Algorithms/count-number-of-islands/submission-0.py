class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        row, col = len(grid), len(grid[0])
        island = 0
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"
            while q:
                rown, coln = q.popleft()
                for i, j in directions:
                    ri, cj = rown + i, coln + j
                    if ri in range(row) and cj in range(col) and grid[ri][cj] == "1":
                        q.append((ri, cj))
                        grid[ri][cj] = "0"
            
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    bfs(r, c)
                    island += 1
        return island