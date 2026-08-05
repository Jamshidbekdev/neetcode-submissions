class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(1, len(nums)):
            gap = nums[i] - nums[i - 1] - 1
            if k > gap:
                k -= gap
            else:
                return nums[i - 1] + k
        return nums[-1] + k