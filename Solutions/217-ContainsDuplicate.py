class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Set doesn't keep duplicates
        return len(set(nums)) != len(nums)