class Solution:
    def add(self, a: int, b: int) -> int:
        x=0xffffffff

        a,b=a&x,b&x
        print(bin(b))
        while b!=0:
            a,b=(a^b),(a&b)<<1& x
        return a  if a<=0x7fffffff else  ~(a&x)
test=Solution()
a=1
b=-2
d=test.add(a,b)
print(d)