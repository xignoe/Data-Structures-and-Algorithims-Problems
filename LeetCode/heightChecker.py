class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = []
        for i in heights:
            sortedHeights.append(i)
        count = 0
        sortedHeights.sort()
        for i in range(len(heights)):
            if heights[i] != sortedHeights[i]:
                count += 1
        
        return count