class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        ug = [2, 3, 5]
        for factor in ug:
            while n % factor == 0:
                n /= factor
        return n == 1
