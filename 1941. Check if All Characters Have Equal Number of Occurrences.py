class Solution(object):
    def areOccurrencesEqual(self, s):
        char=[]
        lnt=[]
        for i in range(len(s)):
            char.append(s[i])
        set(char)
        for i in range(len(char)):
            cnt=0
            cnt=s.count(char[i])
            lnt.append(cnt)
        if lnt==[cnt]*len(char):
            return True
        else:
            return False