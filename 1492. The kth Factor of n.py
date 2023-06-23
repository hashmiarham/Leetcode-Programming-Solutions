class Solution(object):
    def kthFactor(self, n, k):
        fact=[]
        for i in range(1,n+1):
            if n%i==0:
                fact.append(i)
        if k>len(fact):
            return -1
        else:
            return fact[k-1]