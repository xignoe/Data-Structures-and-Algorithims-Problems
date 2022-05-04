class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        charMap = {}
        maxChar = 0
        windowStart = 0
        maxLen = 0
        
        for i in range(len(s)):
            rightChar = s[i]
            if rightChar not in charMap:
                charMap[rightChar] = 0
            charMap[rightChar] += 1
            
            maxChar = max(maxChar, charMap[rightChar])
            
            if (i - windowStart + 1 - maxChar) > k:
                leftChar = s[windowStart]
                charMap[leftChar] -= 1
                windowStart += 1
                
            maxLen = max(maxLen, i - windowStart + 1)
        
        return maxLen