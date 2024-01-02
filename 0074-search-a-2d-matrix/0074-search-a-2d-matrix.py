class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        top = 0
        bottom = ROWS - 1
        
        while top <= bottom:
            midRow = (top + bottom) // 2
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bottom = midRow - 1
            else:
                break
        
        # to remember
        if not (top <= bottom):
            return False
        
        # this is the row we are going to perform our operation.
        row = (top + bottom)//2
        left = 0
        right = COLS-1
        
        while left <= right:
            mid = (left +  right) // 2
            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else: 
                return True
        return False
        