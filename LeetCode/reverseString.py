class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        count = []
        for i in range(len(s)):
            count.append(s[i])
        for i in range(len(s)):
            s[i] = count[len(s) - i - 1]