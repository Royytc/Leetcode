丞
        sortedNum=sorted(nums)
        if  len(sortednum)%2:
            return False
        else:
            sum=0
            for i in range(0,len(sortedSNum),2):
                sum+=sortedNum[i]
        return sum
            