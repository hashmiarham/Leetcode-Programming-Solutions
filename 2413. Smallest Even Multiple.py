class Solution(object):
    def smallestEvenMultiple(self, n):
        smallest_multiple = 4587952
        for i in range(1, n * 2 + 1):
            if i % 2 == 0 and i % n == 0:
                smallest_multiple = min(smallest_multiple, i)
        
        return smallest_multiple
