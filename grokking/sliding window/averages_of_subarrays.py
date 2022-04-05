def find_averages_of_subarrays(k, arr):
    resultArray = []
    for i in range(len(arr) - k + 1):
        sumNum = 0.0
        for j in range(i, i+k):
            sumNum += arr[j]
        
        resultArray.append(sumNum / k)

    return resultArray

def main():
    print(find_averages_of_subarrays(5,[1,2,3,4,5,6,7,8]))

main()