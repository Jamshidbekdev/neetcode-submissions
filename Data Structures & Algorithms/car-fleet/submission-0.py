class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        orders = []
        stack = []
        for p, s in zip(position, speed):
            orders.append((p, (target - p) / s))
        orders.sort(reverse=True)
        for (p, t) in orders:
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)