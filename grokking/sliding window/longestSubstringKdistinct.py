def longestSubstring(wordle, k):
    count = 1
    subStr = []
    currentMax = 0

    for i in range(len(wordle)):
        while wordle[i] != wordle[count] and count < len(wordle):
            subStr.append(wordle[i])
            count += 1
            currentMax = len(subStr)
        count = i

    

    print(set(wordle))
    return currentMax

print(longestSubstring("araaci", 2))