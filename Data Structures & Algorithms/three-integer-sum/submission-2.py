class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            p_1 = i+1
            p_2 = len(nums)-1
            while(p_1<p_2):
                value = nums[p_1]+nums[p_2]
                if value == target:
                    ans.append([nums[i], nums[p_1], nums[p_2]])
                    p_1 += 1
                    while(nums[p_1]==nums[p_1-1] and p_1 < len(nums)-1):
                        p_1 += 1
                    p_2 -= 1
                if value < target:
                    p_1 += 1
                if value > target:
                    p_2 -= 1
        return ans