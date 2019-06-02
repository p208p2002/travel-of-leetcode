class Solution:
    def judgePalindromic(self,s:str):
        if(len(s)==2 and s[0] == s[1]):
            return True
        elif(len(s)==2 and s[0] != s[1]):
            return False
        elif(len(s)==0 or len(s)==1):
            return True

        head = s[0]
        end = s[len(s)-1]
        while(1):
            if(head == end):
                return self.judgePalindromic(s[1:-1])
            else:
                return False
        return False

    def longestPalindrome(self, s: str) -> str:
        if(s == ''):
            return ''
        headIndex = 0
        rec = s[0]
        while(len(s) != (headIndex+1)):
            ###
            for i in range(len(s),0,-1):
                if(s[headIndex] == s[i-1]):
                    testStr = s[headIndex:i]
                    #print(testStr,rec)
                    if(self.judgePalindromic(testStr) and (len(testStr) > len(rec))):
                            rec = testStr
                    #break
            headIndex += 1
        return rec