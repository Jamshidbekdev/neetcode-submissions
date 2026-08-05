class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        left, right = 0, m * n - 1
        while left <= right:
            middle = (left + right) // 2
            r = middle // m 
            c = middle % m
            if matrix[r][c] > target:
                right = middle - 1
            elif matrix[r][c] < target:
                left = middle + 1
            else:
                return True
        return False
