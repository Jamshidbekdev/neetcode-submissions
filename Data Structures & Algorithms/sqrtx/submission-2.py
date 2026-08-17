class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        # [1,2,3,4,5,6,7,8,9,10,11,12,13]
        #        l r
        #        m
        #        m          
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1
        return r

         