class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        result = -1
        for index, value in mp.items():
            if value == 1:
                result = max(result, index)
        return result