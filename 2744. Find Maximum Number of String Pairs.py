class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        cnt=0
        for i in range(len(words)):
            for j in range(len(words)):
                if (words[i]==words[j] or words[i]==words[j][::-1]) and i!=j:
                    cnt+=1
        return int(cnt/2)