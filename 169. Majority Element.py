class Solution(object):
    def majorityElement(self, nums):
        sets=set(nums)
        maxc=0
        maxe=0
        for num in sets:
            if nums.count(num)>maxc:
                maxc=nums.count(num)
                maxe=num
        return maxe