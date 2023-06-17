class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        c=0
        for i in range(len(items)):
            citm=items[i]
            if(ruleKey=="type"):
                if(citm[0]==ruleValue):
                    c+=1
            elif(ruleKey=="color"):
                if(citm[1]==ruleValue):
                    c+=1
            elif(ruleKey=="name"):
                if(citm[2]==ruleValue):
                    c+=1
        return c