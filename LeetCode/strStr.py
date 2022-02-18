class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" and haystack == "":
            return 0
        if needle != None and haystack == "":
            return -1
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle[0:len(needle)]:
                return i
            elif needle not in haystack:
                return -1