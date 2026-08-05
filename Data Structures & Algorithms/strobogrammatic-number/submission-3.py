class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        left, right = 0, len(num) - 1
        valid_same = {'0', '1', '8'}
        while left <= right:
            if (num[left] == num[right] and num[left] in valid_same) or (num[left] == '6' and num[right] == '9') or (num[left] == '9' and num[right] == '6'):
                left += 1
                right -= 1
            else:
                return False
        return True