class Solution(object):
    def repeatedCharacter(self, s):
        dic={}
        for a in s:
            if a not in dic.keys():
                dic[a]=1
            else:
                dic[a]+=1
            for b in dic.keys():
                if dic[b]==2:
                    return b