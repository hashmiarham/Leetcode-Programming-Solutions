class Solution(object):
    def subtractProductAndSum(self, n):
        prod = 1
        sums = 0
        while n != 0:      
            last = n % 10   
            prod *= last    
            sums += last    
            n =n//10        
        return prod - sums 