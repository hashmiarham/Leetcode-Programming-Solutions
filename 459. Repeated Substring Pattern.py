class Solution(object):
    def repeatedSubstringPattern(self, s):
        l=len(s)
        for i in range(1,l):
            ss=s[:i:]
            if ss*(l//len(ss))==s:
                return True
        return False