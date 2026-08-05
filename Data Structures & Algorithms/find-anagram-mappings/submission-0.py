class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = count2 = {}
        result = []
        for index, num in enumerate(nums1):
            count1[num] = index
        for index, num in enumerate(nums2):
            count2[num] = index
        for index, value in enumerate(nums1):
            result.append(count2[value])
        print(count1)
        print(count2)
        return result