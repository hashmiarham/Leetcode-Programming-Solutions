class Solution(object):
    def capitalizeTitle(self, title):
        arr=[a for a in title.split()]
        res=""
        for i in range(len(arr)):
            if len(arr[i])>2:
                if i!=len(arr)-1:
                    res+=arr[i].capitalize()+" "
                else:
                    res+=arr[i].capitalize()
            else:
                if i!=len(arr)-1:
                    res+=arr[i].lower()+" "
                else:
                    res+=arr[i].lower()
        return res
        