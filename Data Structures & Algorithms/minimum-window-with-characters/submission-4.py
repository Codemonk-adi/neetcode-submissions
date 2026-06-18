from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isValidWindow(count_t,count_window):
            for (char, count) in count_t.items():
                if count > count_window.get(char,0):
                    return False
            return True
        count_t = {}
        count_window = {}
        for char in t:
            count_t[char] = count_t.get(char,0) + 1
        for char in s[:len(t)]:
            count_window[char] = count_window.get(char,0) + 1
        ans = ""
        l = 0
        r = len(t)-1
        while r < len(s):
            while isValidWindow(count_t, count_window):
                if ans == "" or len(s[l:r+1]) < len(ans):
                    ans = s[l:r+1]
                count_window[s[l]]-=1
                l += 1
            r += 1
            if r < len(s):
                count_window[s[r]]=count_window.get(s[r],0)+1
        return ans