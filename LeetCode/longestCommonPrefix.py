class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minStr = min(strs)
        maxStr = max(strs)
        
        i = 0
        
        while i < len(minStr) and i < len(maxStr) and minStr[i] == maxStr[i]:
            i += 1
            
        return maxStr[:i]