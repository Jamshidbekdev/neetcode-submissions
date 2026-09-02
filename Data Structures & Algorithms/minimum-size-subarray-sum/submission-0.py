class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        summ = 0
        min_len = float('inf')
        while r < len(nums):
            summ += nums[r]
            while target <= summ:
                min_len = min(min_len, r - l + 1)
                summ -= nums[l]
                l += 1
            r += 1
        return min_len if min_len != float('inf') else 0