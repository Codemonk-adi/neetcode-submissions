from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        counter_s1 = Counter(s1)
        counter_s2 = Counter()
        l = 0
        for r, char in enumerate(s2):
            counter_s2[char]+=1
            if counter_s2 == counter_s1:
                return True
            while counter_s2[char]>counter_s1[char]:
                counter_s2[s2[l]] -= 1
                l += 1
            else:
                r += 1
        return False