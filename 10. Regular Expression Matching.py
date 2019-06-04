import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        try:
            res = re.match(p+'$',s)
            res = res[0]
            return True
        except:
            return False
