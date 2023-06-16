class Solution(object):
    def reverse(self, x):
        s = str(x)
        if(s[0]=="-"):
            b=True
            ss=s[1:]
            sr=ss[::-1]
            n=int((sr))*(-1)
            if(n<(-2**31)):
                return 0
            else:
                return n
        
        c=int(s[::-1])
        if(c>(2**31)-1):
            return 0
        else:
            return c