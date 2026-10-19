class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        left, right = 0, 1
        while right < len(nums):
            if abs(nums[left] - nums[right]) != 1:
                return False
            left += 1
            right += 1
        return True