class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1

        while(numbers[i]+numbers[j]!=target):
            current_sum = numbers[i]+numbers[j]
            if current_sum < target:
                i += 1
            if current_sum > target:
                j -= 1
        return [i+1,j+1]