class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        if nums[0] > 1 or not 1 in nums:
            return 1

        for item in nums:
            if item + 1 > 0 and (not item + 1 in nums):
                return item + 1
        return nums[-1] + 1 if nums[-1] + 1 > 0 else 1