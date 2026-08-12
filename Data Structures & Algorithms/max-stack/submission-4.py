class MaxStack:

    def __init__(self):
        self.stack = []
        self.maxAt = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        current_max = x if not self.maxAt else max(x, self.maxAt[-1])
        self.maxAt.append(current_max)

    def pop(self) -> int:
        self.maxAt.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxAt[-1]

    def popMax(self) -> int:
        topMax = self.maxAt[-1]
        buffer = []
        while self.stack and self.stack[-1] != topMax:
            buffer.append(self.stack[-1])
            self.pop()
        self.pop()
        while buffer:
            self.push(buffer.pop())
        return topMax
