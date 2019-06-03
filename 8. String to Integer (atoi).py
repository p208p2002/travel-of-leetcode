import re
class Solution:
    def myAtoi(self, str: str) -> int:
        prog = re.compile(r"^[0-9]+|^-[0-9]+|^ +-[0-9]+|^ +[0-9]+|\+[0-9]+| +\+[0-9]+")
        result = prog.match(str)
        try:
            result = result[0]
        except:
            result = 0

        result = int(result)
        upRange = 2**31-1
        downRange = 2**31*-1

        if(result>upRange):
            return upRange
        elif(result<downRange):
            return downRange

        return result