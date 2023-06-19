class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=[]
        for i in range(len(candies)):
            nc=candies[i]+extraCandies
            cnt=0
            for j in range(len(candies)):
                if(nc<candies[j]):
                    cnt+=1
            if (cnt>0):
                result.append(False)
            else:
                result.append(True)
        return result