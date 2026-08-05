class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        arr = list(s)
        cnt = 0  # extra ( parentheses
        for i, v in enumerate(s):
            if v == "(":
                stack.append(i)
            elif v == ")":
                if stack: 
                    stack.pop()
                else:
                    arr[i] = ''
        while stack:
            arr[stack.pop()] = ''
        return ''.join(arr)