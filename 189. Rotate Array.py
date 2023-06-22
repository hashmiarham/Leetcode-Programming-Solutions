class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # To handle cases where k > n

        narr = []
        for i in range(n):
            narr.append(nums[(i - k) % n])

        for i in range(n):
            nums[i] = narr[i]