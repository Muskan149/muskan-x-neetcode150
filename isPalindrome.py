class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for char in s.lower():
            if char.isalnum():
                s_new += char
        
        for i, char in enumerate(s_new):
            if char != s_new[-(i + 1)]:
                return False
        
        return True
