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
            if ((s[i].lower() in vowels) and (s[j].lower() in vowels)):
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i = i + 1
                j = j - 1

            if (s[i].lower() not in vowels):
                i = i + 1
            elif (s[j].lower() not in vowels):
                j = j - 1

        return ''.join(s)

        
            