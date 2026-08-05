class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        result = 0
        for num in nums:
            count = 1
            if num - 1 not in store:
                while num + count in store:
                    count+=1
            result = max(result, count)
        return result