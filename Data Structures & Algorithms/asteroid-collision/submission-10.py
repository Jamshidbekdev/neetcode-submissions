class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for item in asteroids:
            if stack and item < 0 and stack[-1] > 0:
                while stack and stack[-1] > 0 and stack[-1] < abs(item):
                    stack.pop()
                if not stack:    
                    stack.append(item)
                elif stack[-1] < abs(item):
                    stack.append(item)
                if stack and stack[-1] == abs(item):
                    stack.pop()
            else:
                stack.append(item)
        return stack
            