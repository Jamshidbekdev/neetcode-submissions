class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            # [3,4,5,6,1,2]
            #  l     m   r
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[mid] >= nums[l]:
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] > target or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return False