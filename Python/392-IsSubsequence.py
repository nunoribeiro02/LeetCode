class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = 0

        while (r < len(s) and l < len(t) ):
            if (s[r] == t[l]):
                r += 1
            l += 1
        
        return r == len(s)
        
