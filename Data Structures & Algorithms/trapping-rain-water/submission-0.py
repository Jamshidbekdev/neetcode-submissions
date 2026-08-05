class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0
        result = 0
        while left < right:
            if height[left] > height[right]:
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]
                right -= 1
            else:
                leftMax = max(leftMax, height[left])
                result += leftMax - height[left]
                left += 1
        return result;