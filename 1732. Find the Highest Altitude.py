class Solution(object):
    def largestAltitude(self, gain):
        max=0
        alt=[0]
        for i in range(len(gain)):
            nalt=alt[i]+gain[i]
            if nalt>max:
                max=nalt
            alt.insert(i+1,nalt)
        return max