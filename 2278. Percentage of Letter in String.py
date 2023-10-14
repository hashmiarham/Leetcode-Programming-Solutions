class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        a,c=0,0
        for char in s:
            if char==letter:
                a+=1
                c+=1
            else:
                a+=1
        return int((c/a)*100)