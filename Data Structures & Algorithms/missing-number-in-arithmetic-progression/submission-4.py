class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = (arr[-1] - arr[0]) // len(arr)
        expected = arr[0]
        for item in arr:
            if item != expected:
                return expected
            expected += d
        return expected