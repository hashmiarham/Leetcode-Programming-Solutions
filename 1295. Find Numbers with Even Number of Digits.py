class Solution(object):
    def findNumbers(self, nums):
        cnt=0
        for num in nums:
            if len(str(num))%2==0:
                cnt+=1
        return cnt