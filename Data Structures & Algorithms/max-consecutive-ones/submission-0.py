class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev, i = 0, 0
        result = 0
        while prev < len(nums):
            count = 0
            while i < len(nums) and nums[i] == 1:
                count += 1
                i += 1
            result = max(result, count)
            i += 1
            prev = i
        return result
            