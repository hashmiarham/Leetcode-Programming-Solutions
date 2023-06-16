class Solution(object):
    def isPalindrome(self, x):
        s=str(x)
        ss=s[::-1]
        if(s==ss):
            return True
        else:
            return False