from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        counter_s1 = Counter(s1)
        counter_window = Counter(s2[:len(s1)])
        for i in range(len(s1),len(s2)):
            if counter_window == counter_s1:
                return True
            counter_window[s2[i]]+=1
            counter_window[s2[i-len(s1)]] -= 1
            
        return counter_window == counter_s1