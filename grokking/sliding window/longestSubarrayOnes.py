def longestSubarrayOnes(arr, k):

    max1 = 0
    windowStart = 0
    maxLen = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            max1 += 1
        
        if (i - windowStart - max1 + 1) > k:
            if arr[windowStart] == 1:
                max1 -= 1
            windowStart += 1

        maxLen = max(maxLen, i - windowStart + 1)
        
    return maxLen

print(longestSubarrayOnes([0,1,1,0,0,0,1,1,0,1,1], 2))