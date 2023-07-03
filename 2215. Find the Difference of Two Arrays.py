class Solution(object):
    def findDifference(self, nums1, nums2):
        num1=set(nums1)
        num2=set(nums2)
        lst=[]
        lst.append(num1.difference(num2))
        lst.append(num2.difference(num1))
        return lst