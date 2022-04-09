import math

def findSmallestSubarray(s, arr):
    count = 0
    minSum = math.inf
    subSum = 0

    for i in range(len(arr)):
        subSum += arr[i]
        while subSum >= s:
            minSum = min(minSum, i - count + 1)
            subSum -= arr[count]
            count += 1

    if minSum == math.inf:
        return 0

    return minSum





print(findSmallestSubarray(7, [2,1,5,2,3,2]))

























# import math

# def findSmallestSubarray(s, arr):
#     subSum = 0
#     count = 0
#     smallWin = math.inf

#     for i in range(len(arr)):
#         subSum += arr[i]
#         while subSum >= s:
#             smallWin = (min(smallWin, i - count + 1))
#             subSum -= arr[count]
#             count += 1
#     if smallWin == math.inf:
#         smallWin = 0

#     # print(subArr)
#     # print(subSum)
#     # print(len(subArr))
#     print(smallWin)

# findSmallestSubarray(7, [2,1,5,2,3,2])

