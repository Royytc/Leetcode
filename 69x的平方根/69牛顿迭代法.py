class Solution:
    def mySqrt(self, x):
    
        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x / r) // 2
        return int(r)