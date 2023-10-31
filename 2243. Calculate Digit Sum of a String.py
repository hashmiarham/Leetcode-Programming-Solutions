class Solution:
    def digitSum(self, s, k):
        while len(s) > k:
            new_s = ''
            for i in range(0,len(s), k):
                temp = 0
                for d in s[i:i+k]:
                    temp += int(d)
 
                new_s += str(temp)

            s = new_s
        
        return s