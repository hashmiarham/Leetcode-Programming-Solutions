class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=list(set(nums))
        for a in s:
            if nums.count(a)==1:
                return a