class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxarea = 0

        def dfs(r, c):
            if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                grid[r][c] = 0
                return 1 + dfs(r - 1, c) + dfs(r, c - 1) + dfs(r , c + 1) + dfs(r + 1, c)
            else:
                return 0

        for i in range(rows):
            for j in range(cols):
                maxarea = max(maxarea, dfs(i, j))
        return maxarea