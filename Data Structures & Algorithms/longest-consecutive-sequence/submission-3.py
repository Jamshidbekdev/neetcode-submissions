class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        result = 0
        for num in nums:
            count, current = 0, num
            while current + count in store:
                count+=1
            result = max(count, result)
        return result