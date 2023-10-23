class Solution(object):
    def backspaceCompare(self, s, t):
        a,b=[],[]
        for i in s:
            if i!="#":
                a.append(i)
            else:
                if a:
                    a.pop()
                else:
                    continue
        for i in t:
            if i!="#":
                b.append(i)
            else:
                if b:
                    b.pop()
                else:
                    continue
        if a==b:
            return True
        else:
            return False