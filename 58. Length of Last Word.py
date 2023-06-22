class Solution(object):
    def lengthOfLastWord(self, s):
        arr=[]
        s.strip()
        arr=s.split()
        return len(arr[-1])