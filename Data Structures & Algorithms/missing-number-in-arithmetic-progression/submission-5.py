class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = (arr[-1] - arr[0]) // len(arr)
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] == arr[0] + mid * d:
                lo = mid + 1             
            else:
                hi = mid
        return arr[0] + d * lo