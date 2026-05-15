class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {} # key is (r,c) and value is longest length
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(r, c, prev):
            if r == rows or r < 0 or c == cols or c < 0 or matrix[r][c] <= prev:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            res = 1
            for dr, dc in directions:
                res = max(res, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            #res = max(1, 1 + dfs(r + 1, c, matrix[r][c]), 1 + dfs(r - 1, c), 1 + dfs(r, c + 1), 1 + dfs(r, c - 1))
            dp[(r, c)] = res
            return res

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, -1)

        return max(dp.values())