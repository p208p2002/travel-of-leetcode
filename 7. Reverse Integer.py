class Solution:
    def reverse(self, x: int) -> int:
        backUpX = x
        x = abs(x)
        s = str(x)
        ans = ''
        for i in range(len(s)-1,-1,-1):
            ans = ans + s[i]
        ans = int(ans)
        if(backUpX<0):
            ans = ans*-1

        downRange = 2**31*-1
        upRange = 2**31-1
        if(ans >=upRange or ans<=downRange):
            return 0

        return ans