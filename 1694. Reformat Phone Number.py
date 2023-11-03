class Solution(object):
    def reformatNumber(self, number):
        number = re.sub(r'[^0-9]', '', number)
        res = []
        i = 0
        n = len(number) 
        
        while n > 0:
            if n - 3 > 1 or n - 3 == 0: 
                count = 3
            else: count = 2
            res.append(number[:count])
            number = number[count:]
            n -= count
        return '-'.join(res)