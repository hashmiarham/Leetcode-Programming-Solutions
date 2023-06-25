class Solution(object):
    def addDigits(self, num):
        s=0
        snum=str(num)
        for i in range(len(snum)):
            s+=int(snum[i])
        if s<10:
            return s
        else:
            return self.addDigits(s)