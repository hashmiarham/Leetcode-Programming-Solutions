class Solution:
    def divisorSubstrings(self, num, k):
        c=0
        s = str(num)
        for i in range(len(s)-k+1):
            t = int(s[i:k+i])
            if t!=0 and num%t==0:
                c+=1
        return c