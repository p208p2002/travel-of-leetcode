class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==0):
            return ''

        common = ''
        numOfStrs = len(strs)
        lenOfStrs=[]

        # count each of str's length
        for i in strs:
            lenOfStrs.append(len(i))

        # find the min of length
        minLen = min(lenOfStrs)

        for i in range(minLen):
            temp = []
            for j in range(numOfStrs):
                temp.append(strs[j][i])

            allEq = 1
            for j in range(len(temp)-1):
                # print(temp[j],temp[j+1])
                if(temp[j]!=temp[j+1]):
                    allEq = 0
                    break
            if(allEq):
                common = common + temp[0]
            else:
                break

        return common




