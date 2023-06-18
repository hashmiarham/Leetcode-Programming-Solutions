class Solution(object):
    def truncateSentence(self, s, k):
        arr=[]
        arr=s.split()
        rs=""
        for i in range(k):
            if (i==k-1):
                rs=rs+arr[i]
            else:    
                rs=rs+arr[i]+" "
        return rs
