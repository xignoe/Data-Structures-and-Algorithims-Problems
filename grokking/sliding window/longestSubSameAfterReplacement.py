def longestSubSameAfterReplacement(word, k):

    charMax = 0
    charMap = {}
    windowStart = 0
    maxLen = 0

    for i in range(len(word)):
        rightChar = word[i]
        if rightChar not in charMap:
            charMap[rightChar] = 0
        charMap[rightChar] += 1

        charMax = max(charMax, charMap[rightChar])

        if (i - windowStart - charMax + 1) > k:
            leftChar = windowStart
            leftChar -= 1
            windowStart += 1

        maxLen = max(maxLen, i - windowStart + 1)

    return maxLen

print(longestSubSameAfterReplacement("aabccbb", 2))
print(longestSubSameAfterReplacement("abbcb", 1))
print(longestSubSameAfterReplacement("abccb", 1))
