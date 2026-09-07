class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, 0
        count = 0
        curr_sum = 0
        while r < len(arr):
            curr_sum += arr[r]
            if r - l + 1 == k:
                if curr_sum / k >= threshold:
                    count += 1
                curr_sum -= arr[l]
                l += 1
            r += 1
        return count