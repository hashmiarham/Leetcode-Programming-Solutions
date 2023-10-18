class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        l=len(startTime)
        cnt=0
        for i in range(l):
            if endTime[i]>=queryTime:
                if startTime[i]<=queryTime:
                    cnt+=1
        return cnt