class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        startWindow = 0
        charMap = {}
        totalFruits = 0
        
        for i in range(len(fruits)):
            rightChar = fruits[i]
            if rightChar not in charMap:
                charMap[rightChar] = 0
            charMap[rightChar] += 1
            
            while len(charMap) > 2:
                leftChar = fruits[startWindow]
                charMap[leftChar] -= 1
                if charMap[leftChar] == 0:
                    del charMap[leftChar]
                startWindow += 1
        
            totalFruits = max(totalFruits, i - startWindow + 1)
        
        return totalFruits