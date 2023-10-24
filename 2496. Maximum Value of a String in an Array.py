class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        
        max_val, cur_val = -1, 0
        
        def hasDigits(word):
            return bool(re.search(r'\d', word))
        
        def hasChars(word):
            return bool(re.search(r'[a-z]', word))
        
        for word in strs:
            if hasDigits(word) and hasChars(word):
                cur_val = len(word)
            elif hasDigits(word) and not hasChars(word):
                cur_val = int(word)
            else:
                cur_val = len(word)
                
            max_val = max(max_val, cur_val)
            
        return max_val