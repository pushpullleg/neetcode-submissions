class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        #print(rows,cols)
        for i in range(rows):
            l = 0        #left
            r = cols-1   # right
            maxval = matrix[i][cols - 1]
            if maxval == target:
                return True
            elif maxval > target:
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
        return False