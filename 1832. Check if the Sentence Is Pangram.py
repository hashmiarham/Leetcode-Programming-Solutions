class Solution:
    def checkIfPangram(self, sentence):
        s=set(sentence)
        for i in range(26):
            if chr(97+i) not in s:
                return False
        return True