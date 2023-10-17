class Solution(object):
    def digitCount(self, nums):
        for i in range(len(nums)):
            if nums.count(str(i))!=int(nums[i]):
                return False
        return True