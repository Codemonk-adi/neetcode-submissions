from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq_mp = Counter()
        ans = 0
        l = 0
        r = 0
        for r, char in enumerate(s):
            freq_mp[char]+=1
            maxf = freq_mp.most_common(1)[0][1]

            while(r-l+1)-maxf > k:
                freq_mp[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
