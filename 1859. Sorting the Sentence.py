class Solution(object):
    def sortSentence(self, s):
        arr = s.split()
        narr = [''] * len(arr)
        for word in arr:
            n = int(word[-1])
            narr[n - 1] = word[:-1]
        return ' '.join(narr)