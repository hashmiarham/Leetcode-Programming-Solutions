class Solution:
    def checkString(self, s: str) -> bool:
        if s=="".join(sorted(s)):
            return True
        else:
            return False