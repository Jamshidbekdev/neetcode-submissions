class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] + nums[i] + nums[j] > target:
                        right -= 1
                    elif nums[left] + nums[right] + nums[i] + nums[j] < target:
                        left += 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[right + 1] == nums[right]:
                            right -= 1
        return result