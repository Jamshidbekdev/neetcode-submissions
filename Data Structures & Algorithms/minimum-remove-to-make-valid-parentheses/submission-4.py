class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        arr = list(s)
        count = 0
        for i, v in enumerate(s):
            if v == '(':
                count += 1
            elif v == ')' and count > 0:
                count -= 1
            elif v == ')':
                arr[i] = ''
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == '(' and count > 0:
                count -= 1
                arr[i] = ''
        return ''.join(arr)
