class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLUMN = len(matrix), len(matrix[0])

        top_row, bot_row = 0, ROWS - 1 #mistake variable mistake, initialisation missed

        while top_row <= bot_row:
            mid_row = (top_row + bot_row) // 2

            if matrix[mid_row][-1] < target:
                top_row = mid_row + 1 #mistake this is repeating with just adding one 
 
            elif matrix[mid_row][0] > target:
                bot_row = mid_row - 1
            
            else:
                break

        if not (top_row <= bot_row):
            return False

        l, r = 0, len(matrix[0]) - 1
        mid_row = (top_row + bot_row) // 2 # m used 
        while l <= r:
            c = (l + r) // 2
            if matrix[mid_row][c] > target :
                r = c - 1
            elif matrix[mid_row][c] < target:
                l = c + 1
            else:
                return True
        
        return False 

        