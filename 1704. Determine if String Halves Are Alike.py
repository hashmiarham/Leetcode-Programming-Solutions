class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a,b=s[:(len(s)//2):],s[(len(s)//2)::]
        lv,rv=0,0
        for v in range(len(b)):
            if a[v] in ['a','e','i','o','u','A','E','I','O','U']:
                lv+=1
            if b[v] in ['a','e','i','o','u','A','E','I','O','U']:
                rv+=1
        if lv==rv:
            return True
        else:
            return False