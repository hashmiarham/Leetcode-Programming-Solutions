class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        cnt=0
        for i in range(len(jewels)):
            tbc=jewels[i]
            for j in range(len(stones)):
                if(stones[j]==tbc):
                    cnt+=1
        return cnt