class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        firstRow = False # variable to indicate 1st row has 0
        firstCol = False # variable to indicate 1st col has 0
        for c in range(n):
            if matrix[0][c] == 0:
                firstRow = True
        for r in range(m):
            if matrix[r][0] == 0:
                firstCol = True
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if firstRow:
            for c in range(n):
                matrix[0][c] = 0
        if firstCol:
            for r in range(m):
                matrix[r][0] = 0
        print(matrix)