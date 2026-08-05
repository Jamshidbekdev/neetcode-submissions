class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        index = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                index = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return index + len(nums) // 2 < len(nums) and nums[index + len(nums) // 2] == target