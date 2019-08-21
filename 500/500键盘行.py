class Solution(object):
    def findWords(self, words):
        result=[]
        set1=set("qwertyuiop")
        set2=set("asdfghjkl")
        set3=set("zxcvbnm")
        for i in words:
            wordLower=i.lower()
            setr=set(wordLower)
            if setr<=set1 or setr <=set2 or setr <=set3:
                result.append(i)
        return result
a=Solution()
b=a.findWords(["Hello","Alaska","Dad","Peace"])
print(b)

        