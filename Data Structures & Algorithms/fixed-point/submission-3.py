class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if mid < arr[mid]:
                right = mid - 1
            elif arr[mid] < mid:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
        return ans