class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = []
        for num in nums:
            if num in numbers:
                return True
            numbers.append(num)

        return False