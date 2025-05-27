class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []
        i = 0
        while (i < len(nums)):
            n = nums[i]
            if n not in res:
                res.append(n)
                i += 1
            else:
                nums.pop(i)

        return len(res)