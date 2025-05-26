class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        cur = set()
        left = 0
        for right in range(len(s)):
            c = s[right]
            while (c in cur):
                cur.remove(s[left])
                left += 1

            cur.add(c)
            longest = max(longest, right - left +1)    

        return longest