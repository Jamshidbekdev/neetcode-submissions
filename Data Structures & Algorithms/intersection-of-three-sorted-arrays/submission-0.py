class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        result = []
        mp1 = {}
        mp2 = {}
        for val in arr1:
            mp1[val] = mp1.get(val, 0) + 1
        for val in arr2:
            if mp1.get(val, 0) > 0:
                mp2[val] = mp2.get(val, 0) + 1
                mp1[val] -= 1
        for val in arr3:
            if mp2.get(val, 0) > 0:
                result.append(val)
                mp2[val] -= 1
        return result
