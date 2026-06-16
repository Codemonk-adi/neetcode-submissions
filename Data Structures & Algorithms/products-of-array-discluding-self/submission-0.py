class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        value = 1
        prefix.append(1)
        for num in nums[:-1]:
            value = value*num
            prefix.append(value)

        value = 1
        suffix = []
        suffix.append(1)
        for num in reversed(nums[1:]):
            value = value*num
            suffix.append(value)
        suffix.reverse()
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i])
        return ans