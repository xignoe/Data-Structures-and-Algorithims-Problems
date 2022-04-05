def max_sum_subarray(arr, k):
    resultArr = []

    windowSum = 0.0

    for i in range(k):
        windowSum += arr[i]

    resultArr.append(windowSum)

    for j in range(k, len(arr)):
        windowSum += arr[j]
        windowSum -= arr[j - k]
        resultArr.append(windowSum)

    return max(resultArr)

def main():
    print(max_sum_subarray([2,3,4,1,5], 2))

main()
