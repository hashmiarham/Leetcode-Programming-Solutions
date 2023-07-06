class Solution(object):
    def pivotIndex(self, nums):
        if len(nums)<1 or len(nums)>10**4:
            return -1
        for i in range(len(nums)):
            arr1=nums[:i:]
            arr2=nums[i+1::]
            s1=sum(arr1)
            s2=sum(arr2)
            if s1==s2:
                return i
        return -1