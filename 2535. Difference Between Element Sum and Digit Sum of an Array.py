class Solution(object):
    def differenceOfSum(self, nums):
        ns=0
        ds=0
        for i in range(len(nums)):
            n=nums[i]
            ns+=n
            for j in range(len(str(n))):
                d=str(n)[j]
                ds+=int(d)
        return abs(ns-ds)