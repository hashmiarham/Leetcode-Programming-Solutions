class Solution(object):
    def commonFactors(self, a, b):
        cnt=0
        if a==b:
            for i in range(1,a+1):
                if a%i==0:
                    cnt+=1
            return cnt
        else:
            for i in range(1,max(a,b)+1):
                if a%i==0 and b%i==0:
                    cnt+=1
            return cnt