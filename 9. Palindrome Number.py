class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        elif(x<10):
            return True

        rec = []
        while(x>0):
            rec.append(x%10)
            x=x//10

        head = 0
        end = len(rec)-1
        palindrome = True
        while(head < end):
            if(rec[head] != rec[end]):
                palindrome = False
                break
            head += 1
            end -= 1

        return palindrome


