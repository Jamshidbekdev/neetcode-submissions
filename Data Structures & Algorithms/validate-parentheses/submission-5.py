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
            elif val in mp.values():
                stack.append(val)
            else:
                return False
        return len(stack) == 0
