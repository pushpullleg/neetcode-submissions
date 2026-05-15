class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        path = set()
        def dfs(r, c, idx):
            # this means all our letters are found and crossed last index
            if len(word) == idx:
                return True
            if r < 0 or c < 0 or r >= row or c >= col or word[idx] != board[r][c] or (r, c) in path:
                return False
            path.add((r, c))
            res = (dfs(r, c - 1, idx + 1) or 
            dfs(r, c + 1, idx + 1) or
            dfs(r - 1, c, idx + 1) or
            dfs(r + 1, c, idx + 1))
            path.remove((r, c)) # to undo this path while tracing back up
            return res

    
        for i in range(row):
            for j in range(col):
                # each element in the matrix is checked with start alphabet
                if dfs(i, j, 0):
                    return True
        return False
