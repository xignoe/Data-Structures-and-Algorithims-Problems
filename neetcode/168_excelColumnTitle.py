class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letter = ""
        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            letter += chr(ord('A') + offset)
            columnNumber = (columnNumber - 1) // 26

        return letter[::-1]