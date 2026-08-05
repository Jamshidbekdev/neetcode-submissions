class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = set()
        for i, v in enumerate(nums):
            if v in ans:
                return True
            ans.add(v)
        return False