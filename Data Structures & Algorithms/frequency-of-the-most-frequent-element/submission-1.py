class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, 0
        summ = 0
        best = 0
        while r < len(nums):
            summ += nums[r]
            while nums[r] * (r - l + 1) - summ > k:
                summ -= nums[l] 
                l += 1
            best = max(best, r - l + 1)
            r += 1
        return best