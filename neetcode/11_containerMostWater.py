class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        maxArea = 0

        while left < right:
            width = right - left
            heightC = min(height[left], height[right])
            area = width * heightC

            if area > maxArea:
                maxArea = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea