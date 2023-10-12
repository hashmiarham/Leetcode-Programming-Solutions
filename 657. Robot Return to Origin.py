class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h,v=0,0
        for a in moves:
            if a == "U":
                v+=1
            elif a=="D":
                v-=1
            elif a == "L":
                h-=1
            else:
                h+=1
        if h==0 and v==0:
            return True
        else:
            return False