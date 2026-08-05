class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for index, value in enumerate(nums):
            if target - value in ans:
                return [ans[target - value], index]
            ans[value] = index
        return [0, 0]