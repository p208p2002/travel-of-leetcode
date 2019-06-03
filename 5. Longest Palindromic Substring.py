class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(s == '' or len(s)==1):
            return s

        rec = s[0]
        for i in range(len(s)):
            #single center
            left = i-1
            right = i+1
            try:
                while(s[left] == s[right]):
                    # print("S:",s[left:right+1],left,right)
                    res = s[left:right+1]
                    if(len(res)>len(rec)):
                        rec = res
                    left -= 1
                    right += 1
            except:
                pass

            #dual center
            try:
                if(s[i] == s[i+1]):
                    #
                    res = s[i]+s[i+1]
                    if(len(res)>len(rec)):
                        rec = res
                    #
                    left2 = i-1
                    right2 = i+2
                    while(s[left2] == s[right2]):
                        # print("D:",s[left2:right2+1],left2,right2)
                        res = s[left2:right2+1]
                        if(len(res)>len(rec)):
                            rec = res
                        left2 -= 1
                        right2 += 1
            except:
                pass

        return rec