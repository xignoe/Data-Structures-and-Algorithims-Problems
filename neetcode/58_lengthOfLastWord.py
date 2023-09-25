class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        spaceCount = 0

        for i in range (len(s)):
            if (s[i - 1] == " " and s[i] != " "):
                count = i            
            
        for j in range (len(s) - 1, 0, -1):
            if (s[j] == " " and j > count):
                spaceCount += 1

        return len(s) - count - spaceCount