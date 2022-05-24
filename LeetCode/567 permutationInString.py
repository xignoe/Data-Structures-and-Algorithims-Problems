class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        charMap = {}
        match = 0
        windowStart = 0
        
        for char in s1:
            if char not in charMap:
                charMap[char] = 0
            charMap[char] += 1
            
        for i in range(len(s2)):
            rightChar = s2[i]
            if rightChar in charMap:
                charMap[rightChar] -= 1
                if charMap[rightChar] == 0:
                    match += 1
                    
            if match == len(charMap):
                return True
            
            
            if i >= len(s1) - 1:
                leftChar = s2[windowStart]
                windowStart += 1
                
                if leftChar in charMap:
                    if charMap[leftChar] == 0:
                        match -= 1
                    charMap[leftChar] += 1
                    
        return False


print(permutationInString("oidbcaf", "acb"))