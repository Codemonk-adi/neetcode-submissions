from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq_mp = Counter(s)
        ans = 0
        for unique in freq_mp:
            l = 0
            count = 0
            for r, char in enumerate(s):
                if char == unique:
                    count += 1
                while(r-l+1)-count > k:
                    if s[l] == unique:
                        count -= 1
                    l += 1
                ans = max(ans, r - l + 1)
        return ans
