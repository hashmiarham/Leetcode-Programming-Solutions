class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer, lookup = [], {}
        for idx in range(len(nums)):
            num = nums[idx]
            if num not in lookup: lookup[num] = math.prod(nums[:idx] + nums[idx + 1:])
            answer.append(lookup[num])
        return answer
        