class Solution:
    def calPoints(self, operations: List[str]) -> int:
        finalScore = 0
        stack = []

        for i in range(len(operations)):
            try:
                finalScore += int(operations[i])
                stack.append(int(operations[i]))
                print(operations[i], "isInt")
            except:
                if ((operations[i]) == 'C'):
                    finalScore -= stack[-1]
                    stack.pop()

                if ((operations[i]) == 'D'):
                    finalScore += stack[-1] * 2
                    stack.append(stack[-1] * 2)

                if ((operations[i]) == '+'):
                    finalScore += (stack[-1] + stack[-2])
                    stack.append(stack[-1] + stack[-2])


                print(operations[i])

        print(stack)

        return finalScore