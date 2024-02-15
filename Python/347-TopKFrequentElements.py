class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequent = {}
        res = []

        for n in nums:
            frequent[n] = frequent.get(n, 0) +1 # Get frequency
        
        # Sort frequency
        frequentItems = sorted(frequent.items(), key=lambda item: item[1])
        
        # Get k most frequent
        while (k > 0):
            res.append(frequentItems.pop()[0])
            k -= 1

        return res