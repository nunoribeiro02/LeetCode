import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^0-9a-zA-Z]+', '', s).lower()
        return s == s[::-1]
    

"""
Space: O(1)
Time: O(n), n is the size of the initial string
"""