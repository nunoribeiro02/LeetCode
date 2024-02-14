class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anagrams = {}
        for s in strs:
            count = [0] * 26 # for the 26 characters from a-z
            
            for letter in list(s):
                count[ord(letter) - ord('a')] += 1

            count = tuple(count)
            if count in anagrams:
                anagrams[count].append(s)
            else:
                anagrams[count] = [s]

        return anagrams.values()
    
"""
Space: O(n), 
Time: O(n*m), n is the average size of each string, m is the size of the array
"""