class Solution:
    def reverseWords(self, s: str) -> str:
        arr=[a for a in s.split()]
        return " ".join(arr[::-1])