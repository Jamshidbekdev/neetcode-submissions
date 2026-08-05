class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,4,5,6]
        result = {}

        for index, value in enumerate(nums):
            if target - value in result:
                return [result[target - value], index]
            result[value] = index
        return []
