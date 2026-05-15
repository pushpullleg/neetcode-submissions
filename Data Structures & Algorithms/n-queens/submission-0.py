class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        colset, negset, posset = set(), set(), set()
        res = []

        def backtrack(r):
            if n == r:
                copy = ["".join(row) for row in board]
                #print(copy)
                res.append(copy)
                return

            for c in range(n):
                if c in colset or (r - c) in negset or (r + c) in posset:
                    continue
                colset.add(c)
                negset.add(r - c)
                posset.add(r + c)
                board[r][c] = "Q"
                backtrack(r + 1)
                colset.remove(c)
                negset.remove(r - c)
                posset.remove(r + c)
                board[r][c] = "."
        backtrack(0)
        return res
        