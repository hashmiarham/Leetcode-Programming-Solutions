class Solution(object):
    def countKDifference(self, nums, k):
        cnt=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]-nums[j]==k:
                    cnt+=1
        return cnt