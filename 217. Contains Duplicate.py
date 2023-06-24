class Solution(object):
    def containsDuplicate(self, nums):
        snums=set(nums)
        return len(nums)!=len(snums)