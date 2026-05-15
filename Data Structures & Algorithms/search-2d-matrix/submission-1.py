class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        while top <= bot:
            midr = (top + bot) // 2 
        # move bottom one step above of mid if the 1st value in mid array is less
            if target < matrix[midr][0]:
                bot = midr - 1
        # move top one step below of mid if the last value in mid array is less
            elif target > matrix[midr][-1]:  
                top = midr + 1
            else:
                break

        if not (top <= bot):
            return False
        l, r = 0, cols - 1
       
        while l <= r:
            midc = (l + r) // 2
            if matrix[midr][midc] == target:
                return True
            elif matrix[midr][midc] < target:
                l = midc + 1
            else:
                r = midc - 1
        return False