class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        ans=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if (i < j < k) and (nums[j] - nums[i]==diff) and (nums[k] - nums[j]==diff):
                        ans+=1
        return ans