class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case
        if len(s) != len(t):
            return False
        
        charCount = {}
        for char in s:
            charCount[char] = charCount.get(char, 0) + 1
        
        for char in t:
            if char not in t:
                return False
            charCount[char] = charCount.get(char, 0) - 1
        
        for key in charCount:
            if charCount[key] != 0:
                return False
        
        return True
