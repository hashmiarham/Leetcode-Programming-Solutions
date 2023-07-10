class Solution(object):
    def findTheArrayConcVal(self, nums):
        concat=0
        tba=0
        while(len(nums)>=1):
            if(len(nums)!=1):
                tba=int(str(nums[0])+str(nums[-1]))
                concat+=tba
                nums.pop(0)
                nums.pop(-1)
            else:
                concat+=nums[0]
                break
        return concat