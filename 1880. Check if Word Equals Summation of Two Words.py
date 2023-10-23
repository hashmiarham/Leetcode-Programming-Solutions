class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        alpha="abcdefghijklmnopqrstuvwxyz"
        w1,w2,t="","",""
        for a in firstWord:
            w1+=str(alpha.index(a))
        for b in secondWord:
            w2+=str(alpha.index(b))
        for c in targetWord:
            t+=str(alpha.index(c))
        if int(w1)+int(w2)==int(t):
            return True
        else:
            return False
        