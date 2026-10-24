class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top_row = 0
        right_col = len(matrix[0]) - 1
        bottom_row = len(matrix) - 1
        left_col = 0
        result = []
        while left_col <= right_col and top_row <= bottom_row:
            for col in range(left_col, right_col + 1):
                result.append(matrix[top_row][col])
            top_row += 1
            for row in range(top_row, bottom_row + 1):
                result.append(matrix[row][right_col])
            right_col -= 1
            if top_row <= bottom_row:
                for col in range(right_col, left_col - 1, -1):
                    result.append(matrix[bottom_row][col])
                bottom_row -= 1
            if left_col <= right_col:
                for row in range(bottom_row, top_row - 1, -1):
                    result.append(matrix[row][left_col])
                left_col += 1
        return result