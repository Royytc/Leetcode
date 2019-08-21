class Solution(object):
    def findWords(self, words):
        result=[]
        for i in words:
            lowi=i.lower()
            if lowi.strip("qwertyuiop")=="" or lowi.strip("asdfghjkl")=="" or lowi.strip("zxcvbnm")=="":
                result.append(i)
        return result
a=Solution()
b=a.findWords(["Hello","Alaska","Dad","Peace"])
print(b)

