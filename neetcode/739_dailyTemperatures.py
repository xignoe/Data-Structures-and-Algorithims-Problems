"""""

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 
"""

temperatures = [73,74,75,71,69,72,76,73]

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day
            stack.append(i)

        return result




    
temperatures = [73,74,75,71,69,72,76,73]
solution = Solution()
resultPrint = solution.dailyTemperatures(temperatures)

print(resultPrint)




        # n = len(temperatures)
        # result = [0] * n

        # stack = []
        
        # for i in range(n):
        #     while stack and temperatures[i] > temperatures[stack[-1]]:
        #         prev_day = stack.pop()
        #         result[prev_day] = i - prev_day
        #     stack.append(i)
        

        # return result
    