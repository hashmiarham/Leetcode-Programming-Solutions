class Solution(object):
    def buildArray(self, nums):
        ans=[]
        for i in range(len(nums)):
            a=nums[i]
            ans.append(nums[a])
        return ans