class Solution(object):
    def countBits(self, num):
        count=[0]*(num+1)
        for i in range(1,num+1):
            count[i]=count[i&(i-1)]+1
        return count
            
        