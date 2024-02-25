class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = 1
        zero = False

        """ Zero is the absorvent multiplicand, these are to deal with them """
        if nums.count(0) == 1:
            zero = True

        for n in nums: 
            if (nums.count(0) > 1):
                res = 0
                breaK;

            if (n == 0):
                continue
            res *= n

        for i in range(len(nums)):
            if (zero):
                nums[i] = res if nums[i] == 0 else 0
            else:
                nums[i] = int(res / nums[i]) if nums[i] != 0 else 0

        return nums

"""
Space: O(1)
Time: O(2n) = O(n), n is the size of the initial array
"""
