class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = {}
        for num in nums:
            if numbers.get(num) == True:
                return True
            numbers[num] = True

        return False