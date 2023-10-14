class Solution:

    def countSeniors(self, details: List[str]) -> int:
        cnt=0
        for a in details:
            age=int(a[11:-2:])
            if age>60:
                cnt+=1
        return cnt
        