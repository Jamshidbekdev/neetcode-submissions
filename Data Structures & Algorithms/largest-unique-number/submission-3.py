class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
            result = -1
        for num in nums:
            if count[num] == 1 and num > result:
                result = num
        return result