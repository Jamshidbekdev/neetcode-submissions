class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # [1,7,2,5,4,7,3,6]
        maxx = -1
        left, right = 0, len(heights) - 1
        while left < right:
            s = (right - left) * min(heights[left], heights[right])
            maxx = max(s, maxx)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxx