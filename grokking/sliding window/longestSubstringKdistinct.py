def longestSubstringKDistinct(word, k):
    windowStart = 0
    maxLen = 0
    charMap = {}

    for i in range(len(word)):
        rightChar = word[i]
        if rightChar not in charMap:
            charMap[rightChar] = 0
        charMap[rightChar] += 1

        #Essentially MAKE the subarray
        while len(charMap) > k:
            leftChar = word[windowStart]
            charMap[leftChar] -= 1
            if charMap[leftChar] == 0:
                del charMap[leftChar]
            windowStart += 1
        maxLen = max(maxLen, i - windowStart + 1)
    
    return maxLen


print(longestSubstringKDistinct("araaci", 2))
print(longestSubstringKDistinct("araaci", 1))
print(longestSubstringKDistinct("cbbebi", 3))