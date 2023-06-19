class Solution(object):
    def shuffle(self, nums, n):
        p1=[]
        p2=[]
        nnum=[]
        for i in range(0,n):
            p1.append(nums[i])
        for j in range(n,len(nums)):
            p2.append(nums[j])
        for k in range(n):
            nnum.append(p1[k])
            nnum.append(p2[k])
        return nnum