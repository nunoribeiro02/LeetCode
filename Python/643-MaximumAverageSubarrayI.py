class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        average = sum(nums[left: right]) / k
        averageMax = average
        left = 1

        while (right < len(nums)):
            average = (average * k - nums[left-1] + nums[right]) / k
            if (average > averageMax):
                averageMax = average
            right += 1
            left += 1

        return averageMax

