class Solution(object):
    def isSubsequence(self, s, t):
        cnt=0
        for i in range(len(t)):
            if cnt<len(s) and s[cnt]==t[i]:
                cnt+=1

        return cnt==len(s)