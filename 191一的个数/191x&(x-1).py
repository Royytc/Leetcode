class Solution(object):
    def hammingWeight(self, n):
        count=0
        while n!=0:
            n=n&(n-1)
            count+=1
        return count
a=Solution()
b=a.hammingWeight(0b00000000000000000000000000001011)
print(b)