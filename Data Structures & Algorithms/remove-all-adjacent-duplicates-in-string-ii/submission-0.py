class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for val in s:
            if stack and stack[-1][0] == val:
                stack[-1][1] += 1
            else:
                stack.append([val, 1])
            if stack[-1][1] == k:
                stack.pop()
        result = ''
        for item in stack:
            result += item[0] * item[1]
        return result