class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        row = 0
        while top <= bottom:
            mid1 = (top + bottom) // 2
            if target < matrix[mid1][0]:
                bottom = mid1 - 1
            elif target > matrix[mid1][-1]:
                top = mid1 + 1
            else:
                row = mid1
                break
        
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid2 = (left + right) // 2
            if target == matrix[row][mid2]:
                return True
            elif target < matrix[row][mid2]:
                right = mid2 - 1
            elif target > matrix[row][mid2]:
                left = mid2 + 1
                
        return False