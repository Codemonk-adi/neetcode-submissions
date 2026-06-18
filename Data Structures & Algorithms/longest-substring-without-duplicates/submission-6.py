class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        ans = 0
        current_length = 0
        l = 0
        for i,char in enumerate(s):
            if char in char_index:
                ans = max(current_length, ans)
                l = max(char_index.get(char)+1, l)
            char_index[char] = i
            ans = max(i - l + 1, ans)
        return max(ans,current_length)