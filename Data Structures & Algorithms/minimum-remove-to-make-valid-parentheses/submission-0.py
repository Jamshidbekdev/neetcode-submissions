class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        for i, v in enumerate(s):
            if v == '(':
                stack.append(i)
            elif v == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        to_remove.update(stack)
        result = ''
        for i, v in enumerate(s):
            if i not in to_remove:
                result += v
        return result;