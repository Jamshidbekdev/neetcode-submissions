class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ''
        num = 0
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '[':
                stack.append((num, curr))
                num = 0
                curr = ''
            elif c == ']':
                nn, cc = stack.pop()
                curr = cc + curr * nn
            else:
                curr += c
        return curr

                