class Solution:
    def judgePalindromic(self,s:str):
        if(len(s)<=1):
            return True
        loop = 0
        sLen = len(s)
        while(sLen>=2):
            # print(loop,s)
            head = s[0]
            end = s[sLen-1]

            if(s[0] == s[sLen-1]):
                s = s[1:-1]
                sLen = len(s)
            elif(s[0] != s[sLen-1]):
                return False
            else:
                return False
            loop+=1
        return True


    def longestPalindrome(self, s: str) -> str:
        # print(self.judgePalindromic(s))

        if(s == ''):
            return ''
        headIndex = 0
        rec = s[0]
        sLen = len(s)
        rLen = len(rec)

        while(len(s) != (headIndex+1)):
            for i in range(sLen,0,-1):
                if(headIndex == i-1):
                    break
                elif(rLen>=sLen-(headIndex)):
                    return rec
                elif(s[headIndex] == s[i-1]):
                    testStr = s[headIndex:i]
                    tLen = len(testStr)
                    if(tLen<rLen):
                        continue
                    elif(self.judgePalindromic(testStr) and (tLen > rLen)):
                        # print(testStr,rec)
                        rec = testStr
                        rLen = len(rec)
                    #break
            headIndex += 1
        return rec