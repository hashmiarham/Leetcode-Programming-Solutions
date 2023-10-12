class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt=nums.count(0)
        for _ in range(cnt):
            nums.pop(nums.index(0))
        for _ in range(cnt):
            nums.append(0)