class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[r] > target:
                r -= 1
            elif nums[l] < target:
                l += 1
            elif nums[l] == target and nums[r] == target:
                return (r - l + 1) > len(nums) // 2
            else:
                return False
        return False