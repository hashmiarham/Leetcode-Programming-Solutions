class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        arr=[]
        for i in range(len(nums)):
            b=bin(i)[2::]
            if k==b.count('1'):
                arr.append(nums[i])
        return sum(arr)
