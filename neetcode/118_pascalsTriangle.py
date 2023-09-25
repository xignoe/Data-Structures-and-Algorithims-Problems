class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pasc = [[1]]

        for i in range(numRows - 1):
            helper = [0] + pasc[-1] + [0]
            row = []
            for j in range(len(pasc[-1]) + 1):
                row.append(helper[j] + helper[j + 1])
            pasc.append(row)

        return pasc