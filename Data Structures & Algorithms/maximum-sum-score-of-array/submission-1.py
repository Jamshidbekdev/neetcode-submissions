class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        ans = float("-inf")
        prefix = 0
        suffix = sum(nums)

        for i in range(len(nums)):
            prefix += nums[i]

            if ans < max(prefix,suffix):
                ans = max(prefix,suffix)
            
            suffix -= nums[i]
        
        return ans
