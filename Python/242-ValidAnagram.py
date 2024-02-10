class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)): 
            return False

        letterS = {}
        letterT = {}

        for i in range(len(s)):
            if letterS.get(s[i], -1) == -1:
                letterS[s[i]] = 1
            else:
                letterS[s[i]] += 1

            if letterT.get(t[i], -1) == -1:
                letterT[t[i]] = 1
            else:
                letterT[t[i]] += 1

        return letterS == letterT