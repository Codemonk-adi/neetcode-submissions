class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_str = ""
        for char in s.lower():
            if char.isalnum():
                alpha_str += char
        return alpha_str == alpha_str[::-1]
            