class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        code=[]
        for a in key:
            if a not in code and a!=" ":
                code.append(a)
        sec={}
        for a in range(len(alpha)):
            sec[code[a]]=alpha[a]
        msg=""
        for a in message:
            if (a in sec.keys()):
                msg=msg+sec[a]
            else:
                msg=msg+a
        return msg