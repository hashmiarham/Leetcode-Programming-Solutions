class Solution(object):
    def defangIPaddr(self, address):
        newad=address.replace(".","[.]")
        return newad