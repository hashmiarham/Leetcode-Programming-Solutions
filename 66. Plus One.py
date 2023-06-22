class Solution(object):
    def plusOne(self, digits):
        nr=[]
        n=0
        for i in range(len(digits)):
            n=(10*n)+digits[i]
        n+=1
        sn=str(n)
        for j in range(len(sn)):
            nr.append(int(sn[j]))
        return nr