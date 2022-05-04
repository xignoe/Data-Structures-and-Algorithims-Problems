class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowStart = 0
        charMap = {}
        maxChar = 0
        
        for i in range(len(s)):
            rightChar = s[i]
            
            if rightChar in charMap:
                windowStart = max(windowStart, charMap[rightChar] + 1)
                
            charMap[rightChar] = i
            
            maxChar = max(maxChar, i - windowStart + 1)
            
        return maxChar