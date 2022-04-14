class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        charMap = {}
        windowStart = 0
        maxLen = 0
        
        for i in range(len(s)):
            rightChar = s[i]
            if rightChar not in charMap:
                charMap[rightChar] = 0
            charMap[rightChar] += 1
        
            while len(charMap) > k:
                leftChar = s[windowStart]
                charMap[leftChar] -= 1
                if charMap[leftChar] == 0:
                    del charMap[leftChar]
                windowStart += 1
                
            maxLen = max(maxLen, i - windowStart + 1)
        
        return maxLen