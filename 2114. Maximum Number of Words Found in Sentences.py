class Solution(object):
    def mostWordsFound(self, sentences):
        lsen=[]
        for i in range(len(sentences)):
            csen=sentences[i]
            cnt=csen.count(" ")
            w=cnt+1
            lsen.append(w)
            cnt=0
            w=0
        gr=0
        for i in range(len(lsen)):
            if(lsen[i]>gr):
                gr=lsen[i]
        return gr