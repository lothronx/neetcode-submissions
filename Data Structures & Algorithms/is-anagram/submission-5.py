class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ds = [0] * 26
        dt = [0] * 26

        for i in range(len(s)):
            ds[ord(s[i])-ord("a")] += 1
            dt[ord(t[i])-ord("a")] += 1
        
        return ds == dt


        