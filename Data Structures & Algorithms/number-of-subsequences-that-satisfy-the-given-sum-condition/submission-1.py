class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                count += 2**(right - left) % 1000000007
                left += 1
            else:
                right -= 1
        return count % 1000000007