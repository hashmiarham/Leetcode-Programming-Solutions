class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt=0
        chk=True
        for a in s:
            if a=="|" and chk==True:
                chk=False
            elif a=="|" and chk==False:
                chk=True
            if a=="*" and chk==True:
                cnt+=1

        return cnt