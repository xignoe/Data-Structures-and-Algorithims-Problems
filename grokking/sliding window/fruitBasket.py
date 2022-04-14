def fruitBaskets(fruits):

    charMap = {}
    windowStart = 0
    totalFruits = 0
    

    for i in range(len(fruits)):
        rightChar = fruits[i]
        if rightChar not in charMap:
            charMap[rightChar] = 0
        charMap[rightChar] += 1

        while len(charMap) > 2:
            leftChar = fruits[windowStart]
            charMap[leftChar] -= 1
            if charMap[leftChar] == 0:
                del charMap[leftChar]
            windowStart += 1
        totalFruits = max(totalFruits, i - windowStart + 1)
    
    return totalFruits

print(fruitBaskets(['A','B','C','A','C']))
print(fruitBaskets(['A','B','C','B','B','C']))