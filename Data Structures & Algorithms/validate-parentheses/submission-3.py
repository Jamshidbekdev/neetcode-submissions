class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
        }
        string = s
        stack = []
        for val in string:
            if val in mp:
                if stack and stack[-1] == mp[val]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(val)
        return len(stack) == 0
