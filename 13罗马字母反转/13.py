class Solution(object):
    def romanToInt(self, s):
        dict1={"I":1,"V":5, "X":10,"L":50,"C":100,"D":500,"M":1000}
        dict2={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        sum=0
        i=0
        while i <len(s):
            if s[i:i+2] in dict2:
                sum+=dict2[s[i:i+2]]
                i+=2
            else: 
                sum+=dict1[s[i]]
                i+=1
        return sum
            
a=Solution()
b=a.romanToInt("IV")
print(b)