class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for elem in s:
            if (elem in ('(', '{', '[')):
                stack.append(elem)
            else :
                if len(stack) == 0 or \
                (elem == ')' and stack[-1] != '(') or \
                (elem == '}' and stack[-1] != '{') or \
                (elem == ']' and stack[-1] != '['):
                    return False
                stack.pop()
            
        return stack == []
    
"""
Space: O(1)
Time: O(n), n is the size of the initial string
"""