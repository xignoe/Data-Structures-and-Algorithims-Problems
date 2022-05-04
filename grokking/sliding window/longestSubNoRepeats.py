def longestSubNoRepeats(word):
    windowStart = 0
    charMap = {}
    maxLen = 0
    
    for i in range(len(word)):
        rightChar = word[i]

        if rightChar in charMap:
            windowStart = max(windowStart, charMap[rightChar] + 1)

        charMap[rightChar] = i
        
        maxLen = max(maxLen, i - windowStart + 1)

    return maxLen
 

print(longestSubNoRepeats("aabccbb"))