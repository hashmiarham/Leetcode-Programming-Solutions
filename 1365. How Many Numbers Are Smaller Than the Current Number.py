class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        arr = []
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    cnt += 1
            arr.append(cnt)
        return arr