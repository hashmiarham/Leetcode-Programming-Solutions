class Solution(object):
    def reverseWords(self, s):
        arr=s.split()
        sntc=""
        for i in range(len(arr)):
            a=arr[i]
            if i!=0:
                sntc+=" "
            sntc+=a[::-1]
        return sntc