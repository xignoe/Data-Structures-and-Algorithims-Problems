class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(num):
            sN = str(num)
            arr = []
            sumN = 0
            for i in range(len(sN)):
                arr.append(sN[i])

            for j in range(len(arr)):
                arr[j] = int(arr[j]) * int(arr[j])
                sumN += arr[j]

            return sumN

        slow = n
        fast = sum_of_squares(n)

        while fast != 1 and slow != fast:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))

        return fast == 1