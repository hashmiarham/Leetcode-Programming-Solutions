class Solution(object):
    def sortArrayByParity(self, nums):
        res=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                res.insert(0,nums[i])
            else:
                res.insert(len(nums)-1,nums[i])
        return res