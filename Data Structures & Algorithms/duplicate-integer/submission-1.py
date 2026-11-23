class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for i, v in enumerate(nums):
            if v in result:
                return True
            result.add(v)
        return False