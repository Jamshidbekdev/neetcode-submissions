class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        while l < r:
            midd = (l + r) // 2
            if x - arr[midd] > arr[midd + k] - x:
                l = midd + 1
            else:
                r = midd
        return arr[l: l + k]