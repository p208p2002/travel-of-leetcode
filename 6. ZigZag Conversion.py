class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows <= 1):
            return s
        mainAry = []
        for i in range(numRows):
            mainAry.append([])

        reverse = False
        selectAry = 0

        for i in range(len(s)):
            # print(selectAry)
            mainAry[selectAry].append(s[i])
            #
            if(i!=0 and(selectAry==0 or selectAry==numRows-1)):
                reverse = not reverse
            #
            if(reverse):
                selectAry -= 1
            else:
                selectAry += 1

        # print(mainAry)
        ans = ''
        for i in range(len(mainAry)):
            for j in range(len(mainAry[i])):
                ans = ans+mainAry[i][j]

        return ans