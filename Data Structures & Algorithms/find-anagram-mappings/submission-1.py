class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        result = [0] * len(nums1)
        for index, val in enumerate(nums2):
            count[val] = index
        for index, value in enumerate(nums1):
            result[index] = count[value]
        return result