class Solution:
    def calPoints(self, operations: List[str]) -> int:
        op=[]
        for a in operations:
            if a=="+":
                op.append(sum(op[-2:]))
            elif a=="D":
                op.append(op[-1]*2)
            elif a=="C":
                op.pop()
            else:
                op.append(int(a))
        return sum(op)
        