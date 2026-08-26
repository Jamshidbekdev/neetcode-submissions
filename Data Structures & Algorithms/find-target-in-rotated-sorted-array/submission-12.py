class Solution:
    def search(self, nums: List[int], target: int) -> int:
    #   [3,4,5,6,1,2] 
    #   l    m     r 
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if nums[mid] > target and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[r] >= target and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
        # target = 1 
        # [3,1]
        #  l r 
        #    l      l m r
        #    m      l r
        #          m
        #          r