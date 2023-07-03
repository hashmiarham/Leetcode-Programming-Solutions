class Solution(object):
    def minimizedStringLength(self, s):
        un=set()
        for i in range(len(s)):
            un.add(s[i])
        return len(un)