class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        i = 0
        while i < len(s):
            if stack and s[i] in mapp and mapp[s[i]] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return not len(stack) > 0
