class Solution(object):
    def finalValueAfterOperations(self, operations):
        v=0
        a=operations.count("++X")
        b=operations.count("X++")
        c=operations.count("--X")
        d=operations.count("X--")
        return a+b-c-d