class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -1001
        running_sum = 0
        for i, num in enumerate(nums):
            running_sum += num
            max_sum = max(running_sum, max_sum)
            if running_sum <= 0:
                running_sum = 0
        return max_sum