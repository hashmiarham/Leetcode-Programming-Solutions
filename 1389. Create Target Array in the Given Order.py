class Solution(object):
    def createTargetArray(self, nums, indx):
        target=[]
        for i in range(len(nums)):
            target.insert(indx[i],nums[i])
        return target