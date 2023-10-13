class Solution:
    def isPalindrome(self, s: str) -> bool:
        full=""
        for a in s.lower():
            if a.isalnum():
                full=full+a
        rev=""
        rev=full[::-1]
        print(full)
        print(rev)
        if full == rev:
            return True
        else:
            return False