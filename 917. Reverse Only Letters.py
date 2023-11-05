class Solution(object):
    def reverseOnlyLetters(self, s):
        arr=[]
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                arr.append(s[i])
        for i in range(len(s)):
            if s[i].isalpha()==False:
                arr.insert(i,s[i])
        return ''.join(arr)
        