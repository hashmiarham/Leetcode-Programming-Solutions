class Solution(object):
    def stringMatching(self, words):
        subs=set()
        for i in range(len(words)):
            for j in range(len(words)):
                if words[j] in words[i] and i!=j:
                    subs.add(words[j])
        return subs