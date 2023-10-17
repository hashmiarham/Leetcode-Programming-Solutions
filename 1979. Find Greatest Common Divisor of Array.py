class Solution(object):
    def findGCD(self, nums):
        for i in range(min(nums),0,-1):
            if max(nums)%i==0 and min(nums)%i==0:
                return i