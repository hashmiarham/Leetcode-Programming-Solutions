class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high-low==1:
            return 1
        elif high%2!=0 and low%2!=0 or high%2!=0 or low%2!=0:
            return (high-low)//2+1
        else:
            return (high-low)//2