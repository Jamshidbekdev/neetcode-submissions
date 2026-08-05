class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            middle = (left + right) // 2
            if middle * middle  > x:
                right = middle - 1
            elif middle * middle < x:
                left = middle + 1
            else:
                return middle
        return left - 1
