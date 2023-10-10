class Solution:
    def finalString(self, s: str) -> str:
        res=""
        for a in s:
            if a =='i':
                res=res[::-1]
            else:
                res+=a
        return res