class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        ans = 0
        current_length = 0
        l = 0
        for i,char in enumerate(s):
            if char in char_index:
                ans = max(current_length, ans)
                l = max(char_index.get(char), l)
                current_length = i - l - 1 
            char_index[char] = i
            current_length += 1
        return max(ans,current_length)