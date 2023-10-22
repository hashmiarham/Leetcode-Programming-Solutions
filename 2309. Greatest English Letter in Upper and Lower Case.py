class Solution(object):
    def greatestLetter(self, s):
        s = set(s)
        result = []
        for letter in s:
            if letter == letter.lower():
                if letter.upper() in s:
                    result.append(letter.upper())
            else:
                if letter.lower() in s:
                    result.append(letter)
        if not result:
            return ""
            
        return max(result)