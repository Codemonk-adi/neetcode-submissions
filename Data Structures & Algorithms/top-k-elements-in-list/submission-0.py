import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        freq_list = [(value, key) for key, value in freq_map.items()]
        heapq.heapify_max(freq_list)
        k_frequent_elements = heapq.nlargest(k, freq_list)

        ans = []
        for element in k_frequent_elements :
            ans.append(element[1])
        return ans
        