class Solution(object):
    def restoreString(self, s, indices):
        ns=""
        for i in range(len(indices)):
            n=indices.index(i)
            ns=ns+s[n]
        return ns