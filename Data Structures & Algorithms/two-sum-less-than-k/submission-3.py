class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        result = -1
        while left < right:
            if nums[left] + nums[right] < k:
                result = max(result, nums[left] + nums[right])
            else:
                right -= 1
            left += 1
        return result
                