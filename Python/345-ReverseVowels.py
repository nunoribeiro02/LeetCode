class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i = 0
        j = len(s) -1
        vowels = ('a', 'e', 'i', 'o', 'u')
        
        while (i < j):
            s_i = s[i].lower()
            s_j = s[j].lower()
            if ((s_i in vowels) and (s_j in vowels)):
                s[i], s[j] = s[j], s[i]
                i = i + 1
                j = j - 1

            if (s_i not in vowels):
                i = i + 1
            elif (s_j not in vowels):
                j = j - 1

        return ''.join(s)