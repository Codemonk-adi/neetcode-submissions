class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if map.get(nums[i]) != None:
                return [map.get(nums[i]), i]
            map[target - nums[i]] = i

