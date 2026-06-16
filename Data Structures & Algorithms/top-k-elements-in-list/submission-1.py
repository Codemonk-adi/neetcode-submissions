import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        most_common =  freq_map.most_common(k)
        ans = [i for (i,j) in most_common]
        return ans