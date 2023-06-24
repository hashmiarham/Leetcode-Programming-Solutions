class Solution(object):
    def heightChecker(self, heights):
        cnt=0
        iarr=heights[::]
        iarr.sort()
        for i in range(len(iarr)):
            if heights[i]!=iarr[i]:
                cnt+=1
        return cnt
