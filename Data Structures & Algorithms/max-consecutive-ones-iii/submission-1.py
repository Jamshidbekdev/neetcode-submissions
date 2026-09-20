class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        counter = 0
        result = 0
        while r < len(nums):
            if nums[r] == 0:
                counter += 1
            if counter > k:
                if nums[l] == 0:
                    counter -= 1
                l += 1
            result = max(result, r - l + 1)
            r += 1
        return result