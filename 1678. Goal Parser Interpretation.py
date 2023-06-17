class Solution(object):
    def interpret(self, command):
        cmd=command.replace("()","o").replace("(al)","al")
        return cmd