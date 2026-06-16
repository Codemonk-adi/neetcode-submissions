from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = defaultdict(bool)
        for num in nums:
            exists[num] = True
        starting_nums = []
        for num in nums:
            if exists[num-1] != True:
                starting_nums.append(num)
        
        max_length = 0
        for seed in starting_nums:
            length = 0
            while exists[seed]:
                length += 1
                seed +=1
            if length > max_length:
                max_length = length
        return max_length