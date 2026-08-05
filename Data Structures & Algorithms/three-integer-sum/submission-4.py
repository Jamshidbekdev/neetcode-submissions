class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + target > 0:
                    right -= 1
                elif nums[left] + nums[right] + target < 0:
                    left += 1
                else:
                    result.append([target, nums[left], nums[right]])
                    right -= 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
        return result        