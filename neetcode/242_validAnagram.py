class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False

        sMap = {}
        tMap = {}

        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)

        for j in sMap:
            if sMap[j] != tMap.get(j,0):
                return False

        return True