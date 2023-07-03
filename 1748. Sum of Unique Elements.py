class Solution(object):
    def sumOfUnique(self, nums):
        norep=[]
        sum=0
        for i in range(len(nums)):
            if nums.count(nums[i])==1:
                norep.append(nums[i])
        for i in range(len(norep)):
            sum+=norep[i]
        return sum