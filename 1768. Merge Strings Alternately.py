class Solution(object):
    def mergeAlternately(self, word1, word2):
        ns=""
        for i in range(min(len(word1),len(word2))):
            ns+=word1[i]+word2[i]
        a=word1 if len(word1)>len(word2) else word2
        ns+=a[min(len(word1),len(word2)):max(len(word1),len(word2)):]
        return ns
        