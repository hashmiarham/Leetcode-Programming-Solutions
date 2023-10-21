class Solution:
    def reverseBits(self, a: int) -> int:
        #a=10
        g=""
        while a!=0:
            s=a%2
            a=a//2
            g=str(s)+g
        if len(g)!=32:
            for i in range(abs(32-len(g))):
                g="0"+g
            print(g)
        b=(g)
        r=0
        for i in reversed(range(len(b))):
            r=r+((2**i)*int(b[i]))
        return(r)

