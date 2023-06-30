class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        arr=[]
        arr=sentence.split()
        for val in arr:
            if val.startswith(searchWord):
                return (arr.index(val))+1
        return -1