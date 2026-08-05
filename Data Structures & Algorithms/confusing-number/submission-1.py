class Solution:
    def confusingNumber(self, n: int) -> bool:
        mp = {
            '0':'0',
            '1':'1',
            '6':'9',
            '8':'8',
            '9':'6'
        }
        t = str(n)
        pt = len(t) - 1
        res = ''
        while pt >= 0:
            if not t[pt] in mp:
                return False
            res += mp[t[pt]]
            pt -= 1
        return res != t
