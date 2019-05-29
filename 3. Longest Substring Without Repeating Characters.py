class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = int(len(s))
        maxLen = 0
        while(1):
            if(start == end):
                break
            testStr = s[start:end]
            recAry = [0]*128
            countLen = 0
            loop = 1
            for c in testStr:
                countLen += 1
                asciiOfc = ord(c)
                if(recAry[asciiOfc] == 1):
                    if(countLen>maxLen):
                        maxLen = countLen -1
                    countLen = 0
                    break
                elif(loop == len(testStr)):
                    if(countLen>maxLen):
                        maxLen = countLen
                    countLen = 0
                    break
                else:
                    recAry[asciiOfc] = 1
                loop+=1
            start += 1
        return maxLen