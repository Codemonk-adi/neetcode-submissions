class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = [0]*26
        counter_s2 = [0]*26
        for char in s1:
            counter_s1[ord(char) - ord('a')]+=1
        l = 0
        for r, char in enumerate(s2):
            counter_s2[ord(char) - ord('a')]+=1
            if counter_s2 == counter_s1:
                return True
            if counter_s2[ord(char) - ord('a')]>counter_s1[ord(char) - ord('a')]:
                counter_s2[ord(s2[l]) - ord('a')] -= 1
                l += 1
                while s2[l-1] != char:
                    counter_s2[ord(s2[l]) - ord('a')] -= 1
                    l += 1
            else:
                r += 1
        return False