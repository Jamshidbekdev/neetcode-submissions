class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        operator = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = 10*num + int(c)
            if (not c.isdigit() and c != ' ') or i == len(s) - 1:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-1 * int(num))
                elif operator == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                operator = c
                num = 0
        return sum(stack)