class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_s = [0]*26
        frequency_t = [0]*26
        ord_a = ord('a')
        for letter in s:
            frequency_s[ord(letter)- ord_a]+=1
        
        for letter in t:
            frequency_t[ord(letter)- ord_a]+=1
        for i in range(26):
            if frequency_s[i] != frequency_t[i]:
                return False

        return True

        