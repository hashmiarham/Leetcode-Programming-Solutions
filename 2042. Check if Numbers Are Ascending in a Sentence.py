class Solution(object):
    def areNumbersAscending(self, s):
        arr=[int(a) for a in s.split() if a.isnumeric()]
        for i in range(0,len(arr)-1):
            if arr[i]==arr[i+1] or arr[i]>arr[i+1]:
                return False
        return True