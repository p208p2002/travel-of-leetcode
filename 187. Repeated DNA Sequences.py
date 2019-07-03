class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        allDNA = set()
        out = set()
        for i in range(len(s)-9):
            s2 = s[i:i+10]
            if(s2 in allDNA):
                out.add(s2)
            else:
                allDNA.add(s2)
        return list(out)