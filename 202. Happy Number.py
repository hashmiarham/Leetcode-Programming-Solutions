class Solution(object):
    def isHappy(self, n):
        csum=0
        for i in range(len(str(n))):
            csum+=int(str(n)[i])**2
        if csum==1:
            return True
        elif(csum<5):
            return False
        else:
            return self.isHappy(csum)
