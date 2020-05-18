class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [c for c in s]
        t = [c for c in t]
        
        s = sorted(s, key=lambda c:ord(c), reverse=False)
        t = sorted(t, key=lambda c:ord(c), reverse=False)
        
        s = ''.join(s)
        t = ''.join(t)
        return s == t
