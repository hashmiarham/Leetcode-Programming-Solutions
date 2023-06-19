class Solution(object):
    def maximumWealth(self, accounts):
        maxw=0
        for i in range(len(accounts)):
            ca=accounts[i]
            tb=0
            for j in range(len(ca)):
                tb+=ca[j]
            if tb>maxw:
                maxw=tb
        return maxw