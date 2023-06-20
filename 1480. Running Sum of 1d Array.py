class Solution(object):
    def runningSum(self, nums):
        arr=[]
        c=0
        for i in range(len(nums)):
            c=c+nums[i]
            arr.append(c)
        return arr