class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        max_score = -float('inf')
        for num in nums:
            prefix += num
            suffix = total - prefix + num
            max_score = max(max_score, prefix, suffix)
        return max_score