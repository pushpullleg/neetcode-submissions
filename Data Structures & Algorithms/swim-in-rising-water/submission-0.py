class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set((0, 0))
        minHeap = [[grid[0][0], 0, 0]]
        size = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while minHeap:
            val, r, c = heapq.heappop(minHeap)
            if r == size - 1 and c == size - 1:
                return val
            for rd, cd in directions:
                row, col = rd + r, cd + c
                if row == size or col == size or row < 0 or col < 0 or (row, col) in visited:
                    continue
                heapq.heappush(minHeap, [max(val, grid[row][col]), row, col])
                visited.add((row, col))
