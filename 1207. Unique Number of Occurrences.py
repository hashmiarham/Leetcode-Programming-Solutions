class Solution:
    def uniqueOccurrences(self, arr):

        check = dict()
        for i in arr:
            if i in check:
                check[i]=check[i]+1
            else:
                check[i]=1
        return len(check.values())==len(set(check.values()))