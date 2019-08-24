class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        l=1
        r=x
        res=0
        while l<=r:
            m=(l+r)//2
            if m==x/m:
                return m
            elif m>x/m:
                r=m-1
                res=m
            else:
                l=m+1
                res=m
        return res
a=Solution()
b=a.mySqrt(8)
print(b)