class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for key, num in enumerate(nums):
            if num in mp:
                if abs(key - mp[num]) <= k:
                    return True
            mp[num] = key
        return False