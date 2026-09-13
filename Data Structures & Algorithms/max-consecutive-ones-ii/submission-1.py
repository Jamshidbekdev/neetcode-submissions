class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mp = {}
        max_length = -1
        l, r = 0, 0
        while r < len(nums):
            mp[nums[r]] = mp.get(nums[r], 0) + 1
            while mp.get(0, 0) > 1:
                mp[nums[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length