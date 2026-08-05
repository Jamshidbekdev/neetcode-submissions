class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left, right = 0, len(numbers)
        mp = {}
        for index, number in enumerate(numbers):
            if target - number != number and target - number in mp:
                return [mp[target - number] + 1, index + 1]
            else:
                mp[number] = index
        return [0, 0]