class Solution(object):
    def similarPairs(self, words):
        cnt=0
        for i in range(len(words)):
            word=list(set(list(words[i])))
            for j in range(len(words)):
                if i!=j:
                    nword=list(set(list(words[j])))
                    if word==nword:
                        cnt+=1
        if cnt!=0:
            return cnt//2
        else:
            return cnt