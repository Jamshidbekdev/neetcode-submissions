class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        nums.sort()
        result = 1000
        while r < len(nums):
            if r - l + 1 == k:
                result = min(result, nums[r] - nums[l])
                l += 1
            r += 1
        return result