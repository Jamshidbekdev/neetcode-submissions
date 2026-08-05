class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = (arr[-1] - arr[0]) // len(arr)
        if d == 0:
            return arr[0]
        mp = {}
        for val in arr:
            mp[val] = True
        for item in arr:
            if (item + d) not in mp:
                return item + d
        return -1